# -*- coding: utf-8 -*-
import numpy as np  # version 1.19.0
import matplotlib.pyplot as plt  # version 3.2.2
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

# DATOS GENERADOS LOCALMENTE
X = np.linspace(-100, 100, 100)
Y = 1/(1+np.exp((-X)))
aux = [[x]*100 for x in range(100)]
Z = np.array(aux)

# DATOS DE MUESTRA DE MATPLOTLIB
a, b, c = axes3d.get_test_data(0.05)


def plot_surface(x, y, z=np.array([[i]*100 for i in range(100)]), nombre='Sigmoide 3d'):
    """los datos de z son de una sola dimension (1 z para cada x, y), por defecto
    se incluye una malla de 100 x 100"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z)
    ax.set_title(f"{nombre}")
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def plot_wireframe(x, y, z=np.array([[i]*100 for i in range(100)]), nombre='Sigmoide 3d'):
    """los datos de z son de 2 dimensiones (2 z para cada x, y)"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z)
    ax.set_title(f"{nombre}")
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def plot_scatter(x, y, z=np.array([i for i in range(100)]), nombre='Sigmoide 3d'):
    """los datos de z son de una sola dimension (1 z para cada x, y)"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_title(f"{nombre}")
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def plot_trisurf(x, y, z=np.array([i for i in range(100)]), nombre='Sigmoide 3d'):
    """los datos de z son de una sola dimension (1 z para cada x, y)"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x, y, z)
    ax.set_title(f"{nombre}")
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def plot_voxel(tensor):
    """Ejemplo:
    N1, N2, N3 = 10, 10, 10
    ma = np.random.choice([0, 1, 2, 3, 4], size=(N1, N2, N3), p=[0.2, 0.2, 0.2, 0.2, 0.2])
    plot_voxel(ma)
    """
    fig = plt.figure(figsize=(10, 10))
    ax = plt.gca(projection='3d')
    ax.voxels(tensor)
    plt.show()


def plot_bar(x, y, z=np.array([i for i in range(100)]), nombre='Sigmoide 3d'):
    """los datos de z son de una sola dimension (1 z para cada x, y)"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(x=x, y=z, z=y, dx=1, dy=1, dz=0.1, shade=True)
    ax.set_title(f"{nombre}")
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def plot_contour(x, y, z=np.array([i for i in range(100)])):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    cset = ax.contourf(x, y, z, cmap=cm.coolwarm)
    ax.clabel(cset, fontsize=9, inline=True)
    plt.show()


plot_contour(a, b, c)
