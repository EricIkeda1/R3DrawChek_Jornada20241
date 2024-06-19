import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import plotly.express as px
import numpy as np
import tensorflow as tf
import random

# Defina aqui o caminho dos diretórios de treinamento e validação
train_dir = ''
val_dir = ''

# Exibe a quantidade de imagens nos diretórios (sem subpastas específicas)
print('Total de imagens para treino:', len(os.listdir(train_dir)))
print('Total de imagens para validação:', len(os.listdir(val_dir)))

# Exibe os nomes dos arquivos dentro dos diretórios de treino e validação
train_names = os.listdir(train_dir)
val_names = os.listdir(val_dir)

# Exibe algumas imagens de treinamento
n = 3
for i in range(n):
    img_path = os.path.join(train_dir, train_names[i])
    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.show()

# Exibe algumas imagens de validação
for i in range(n):
    img_path = os.path.join(val_dir, val_names[i])
    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.show()

# Define o tamanho padrão para processamento das imagens
img_size = 128

# Cria instância que lê as imagens diretamente dos diretórios e normaliza os valores das imagens
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)

# Carrega imagens diretamente dos diretórios
train_generator = train_datagen.flow_from_directory(
    train_dir,  # raiz com pastas das categorias
    target_size=(img_size, img_size),  # tamanho a redimensionar imagens
    batch_size=128,  # tamanho dos lotes usados para leitura das imagens
    class_mode='sparse'  # formato das labels
)

val_generator = val_datagen.flow_from_directory(
    val_dir,  # raiz com pastas das categorias
    target_size=(img_size, img_size),  # tamanho a redimensionar imagens
    batch_size=128,  # tamanho dos lotes usados para leitura das imagens
    class_mode='sparse'  # formato das labels
)

# Número máximo de épocas para treinar
n_epochs = 100

# Número de épocas a esperar quando 'para de aprender'
n_patience = 2

# Reinicializa sessão
tf.keras.backend.clear_session()

# Cria uma rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(img_size, img_size, 3)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

print(model.summary())

# Configura os parâmetros de aprendizado
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Espera 'n_patience' épocas para parar o treinamento com base na loss
stopCallback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=n_patience)

# Treina o modelo, separando uma parte dos dados para validação
history = model.fit(train_generator, epochs=n_epochs,
                    validation_data=val_generator,
                    callbacks=[stopCallback])

# Exibe gráficos de perda e acurácia
fig = px.line(x=range(len(history.history['loss'])), y=[history.history['loss'], history.history['val_loss']], labels={'x':'Epoch', 'y':'Loss'})
fig.show()

fig = px.line(x=range(len(history.history['accuracy'])), y=[history.history['accuracy'], history.history['val_accuracy']], labels={'x':'Epoch', 'y':'Accuracy'})
fig.show()

# Reinicializa sessão
tf.keras.backend.clear_session()

# Cria uma nova rede convolucional
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(8, (3, 3), activation='relu', input_shape=(img_size, img_size, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

print(model.summary())

# Configura os parâmetros de aprendizado
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treina o modelo, separando uma parte dos dados para validação
history = model.fit(train_generator, epochs=n_epochs,
                    validation_data=val_generator,
                    callbacks=[stopCallback])

# Exibe gráficos de perda e acurácia
fig = px.line(x=range(len(history.history['loss'])), y=[history.history['loss'], history.history['val_loss']], labels={'x':'Epoch', 'y':'Loss'})
fig.show()

fig = px.line(x=range(len(history.history['accuracy'])), y=[history.history['accuracy'], history.history['val_accuracy']], labels={'x':'Epoch', 'y':'Accuracy'})
fig.show()

# Cria um modelo que recebe uma imagem como entrada e exibe representações intermediárias como saída
successive_outputs = [layer.output for layer in model.layers]
visualization_model = tf.keras.models.Model(inputs=model.input, outputs=successive_outputs)

# Armazena o nome de todas as imagens de treino
img_files = [os.path.join(train_dir, f) for f in train_names]

# Seleciona uma delas aleatoriamente
img_path = random.choice(img_files)

# Identifica imagem selecionada
print('Arquivo selecionado:', img_path.split('/')[-1])

# Carrega e exibe a imagem
img = tf.keras.preprocessing.image.load_img(img_path, target_size=(img_size, img_size))
plt.imshow(img)
plt.show()

# Representa a imagem como numpy array do formato (img_size, img_size, 3)
x = tf.keras.preprocessing.image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x /= 255

# Passa a imagem pela rede e captura todas as representações intermediárias
successive_feature_maps = visualization_model.predict(x)

# Armazena o nome de cada uma das camadas
layer_names = [layer.name for layer in model.layers]

# Plota mapas de características para cada uma das camadas convolucionais
for layer_name, feature_map in zip(layer_names, successive_feature_maps):
    if len(feature_map.shape) == 4:  # mapa de características 4D
        n_features = feature_map.shape[-1]
        size = feature_map.shape[1]
        display_grid = np.zeros((size, size * n_features))
        for i in range(n_features):
            x = feature_map[0, :, :, i]
            x -= x.mean()
            x /= x.std()
            x *= 64
            x += 128
            x = np.clip(x, 0, 255).astype('uint8')
            display_grid[:, i * size : (i + 1) * size] = x
        scale = 20. / n_features
        plt.figure(figsize=(scale * n_features, scale))
        plt.title(layer_name)
        plt.grid(False)
        plt.imshow(display_grid, aspect='auto', cmap='viridis')
        plt.show()
