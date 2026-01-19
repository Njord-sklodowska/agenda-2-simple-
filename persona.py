# generamos el molde o clase
class Persona:
    def __init__(self, nombre , apellido , tel):
        if not nombre.strip():
            raise ValueError("no puede estar vacio")
        elif " " in nombre:
            raise ValueError("no puede contener espacios vacios el nombre")
        
        if not apellido.strip():
            raise ValueError("no puede estar vacio")
        elif " " in apellido:
            raise ValueError("no puede contener espacio vacios el apellido")
        
        if not tel.strip():
            raise ValueError("no puede estar vacio")
        elif " " in tel:
            raise ValueError("no puede contener espacios vacios el numero de tel..")
        
        self._nombre = nombre
        self._apellido = apellido
        self._tel = tel
    
    #property --- solo lectura de los "self"
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    @property
    def tel(self):
        return self._tel
    
    # creamos una funcion para la creacion de los datos 
    # y como estos se muestran!!
    def mostrar_datos(self):
        print(f"el usuario: {self.nombre} , {self.apellido} , {self.tel}")