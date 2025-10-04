# --- Constantes para el modelo Usuario (Perfil) ---

# Asumiendo que 1 es el ID del perfil Administrador en la tabla Perfil
ADMINISTRADOR = 1 
CAJERO = 2
VENDEDOR = 3

# --- Constantes para el modelo DispositivoMovil ---

# Lista de opciones para el campo 'operador' en DispositivoMovil
OPERADORES = [
    ('CLARO', 'Claro'),
    ('MOVISTAR', 'Movistar'),
    ('ENTEL', 'Entel'),
    ('BITEL', 'Bitel'),
    # Puedes agregar más operadores aquí
]