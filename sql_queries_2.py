DDL_QUERY = '''
CREATE TABLE IF NOT EXISTS dim_articulo (
    id_articulo INT,
	id_categoria INT,
    codigo VARCHAR(50),
    nombre VARCHAR(100),
    precio_venta NUMERIC(11,2),
    descripcion VARCHAR(255),
    imagen VARCHAR(20),
    nombre_categoria VARCHAR(50),
    descripcion_categoria VARCHAR(255),
    
    PRIMARY KEY (id_articulo)
);

CREATE TABLE IF NOT EXISTS dim_persona (
    id_persona INT,
	tipo_persona VARCHAR(20),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(20),
    
    PRIMARY KEY (id_persona)
);

CREATE TABLE IF NOT EXISTS dim_usuario (
    id_usuario INT,
	id_rol INT,
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(20),
    clave BLOB ,
    nombre_rol VARCHAR(30),
    descripcion_rol VARCHAR(30),
    
    PRIMARY KEY (id_usuario)
);


CREATE TABLE IF NOT EXISTS dim_fecha (
	fecha DATE, 
    año TINYINT,
	trimestre TINYINT,
    mes TINYINT,
    dia TINYINT,
    dia_de_la_semana TINYINT,
    es_fin_de_semana TINYINT,
    id_fecha INT,
    
    PRIMARY KEY (id_fecha)
);

CREATE TABLE IF NOT EXISTS fact_ventas (
	sk_fact_ventas INT AUTO_INCREMENT, 
	id_detalle_venta INT,
    id_venta INT,
    id_articulo INT REFERENCES dim_articulo(id_articulo),
    id_fecha INT REFERENCES dim_fecha(id_fecha),
    cantidad TINYINT,
    precio NUMERIC(11,2),
    descuento NUMERIC(11,2),
    id_persona INT REFERENCES dim_persona(id_persona),
    id_usuario INT REFERENCES dim_usuario(id_usuario),
    total NUMERIC(11,2),
    impuesto FLOAT,
    
    PRIMARY KEY (sk_fact_ventas)
);

CREATE TABLE IF NOT EXISTS fact_ingresos (
	sk_fact_ingresos INT AUTO_INCREMENT, 
	id_detalle_ingreso INT,
    id_ingreso INT,
    id_articulo INT REFERENCES dim_articulo(id_articulo),
    id_fecha INT REFERENCES dim_fecha(id_fecha),
    cantidad TINYINT,
    precio_unitario NUMERIC(11,2),
    id_proveedor INT REFERENCES dim_persona(id_persona),
    id_usuario INT REFERENCES dim_usuario(id_usuario),
    total NUMERIC(11,2),
    
    PRIMARY KEY (sk_fact_ingresos)
);

'''