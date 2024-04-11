DDL_QUERY = '''
CREATE TABLE IF NOT EXISTS categoria(
    id_categoria INT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE,
    descripcion VARCHAR(255),
    estado_categoria BOOLEAN
);

CREATE TABLE IF NOT EXISTS articulo(
    id_articulo INT PRIMARY KEY,
    id_categoria INT REFERENCES categoria(id_categoria),
    codigo VARCHAR(50),
    nombre VARCHAR(100),
    precio_venta NUMERIC(11,2),
    stock INT,
    descripcion VARCHAR(255),
    imagen VARCHAR(20),
    estado_articulo BOOLEAN
);

CREATE TABLE IF NOT EXISTS persona(
    id_persona INT PRIMARY KEY,
    tipo_persona VARCHAR(20),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS rol(
    id_rol INT PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(30),
    estado_rol BOOLEAN
);

CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INT PRIMARY KEY,
    id_rol INT REFERENCES rol(id_rol),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(20),
    clave BYTEA,
    estado_usuario BOOLEAN
);

CREATE TABLE IF NOT EXISTS ingreso(
    id_ingreso INT PRIMARY KEY,
    id_proveedor INT REFERENCES persona(id_persona),
    id_usuario INT REFERENCES usuario(id_usuario),
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha TIMESTAMP,
    impuesto NUMERIC(4,2),
    total NUMERIC(11,2),
    estado_venta VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS detalle_ingreso(
    id_detalle_ingreso INT PRIMARY KEY,
    id_ingreso INT REFERENCES ingreso(id_ingreso),
    id_articulo INT REFERENCES articulo(id_articulo),
    cantidad INT,
    precio_unitario NUMERIC(11,2)
);

CREATE TABLE IF NOT EXISTS venta(
    id_venta INT PRIMARY KEY,
    id_cliente INT,
    id_usuario INT REFERENCES usuario(id_usuario),
    id_persona INT REFERENCES persona(id_persona),
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha TIMESTAMP,
    impuesto NUMERIC(4,2),
    total NUMERIC(11,2),
    estado_venta VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS detalle_venta(
    id_detalle_venta INT PRIMARY KEY,
    id_venta INT REFERENCES venta(id_venta),
    id_articulo INT REFERENCES articulo(id_articulo),
    cantidad INT,
    precio NUMERIC(11,2),
    descuento NUMERIC(11,2)
);

'''
