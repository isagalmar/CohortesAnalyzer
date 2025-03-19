from langchain.tools import tool
import os
import requests

port = os.getenv("DATAPOINT_PORT")
host = "127.0.0.1"



#Pacientes
@tool
def getAllPacientes():
    """Devuelve los datos de todos los pacientes."""

    req = requests.get(f"http://{host}:{port}/pacientes/")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getPacientePorProvincia(provincia: str):
    """Devuelve los pacientes de una povincia"""

    provincia_n=str(provincia).strip('"\n')

    req = requests.get(f"http://{host}:{port}/pacientes/?provincia={provincia_n}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getPacientePorId(pacienteId:int):
    """Devuelve un paciente cuya id coincida con la pasada"""

    req = requests.get(f"http://{host}:{port}/pacientes/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()
#Pacientes




#Condiciones
@tool
def getAllCondiciones():
    """Devuelve todas las condiciones registradas."""

    req = requests.get(f"http://{host}:{port}/condiciones/")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getCondicionesPorId(pacienteId:int):
    """Devuelve las condiciones cuya id de paciente coincida con la pasada"""

    req = requests.get(f"http://{host}:{port}/condiciones/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()
#Condiciones




#Encuentros
@tool
def getAllEncuentros():
    """Devuelve todos los encuentros registradas."""

    req = requests.get(f"http://{host}:{port}/encuentros/")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getEncuentrosPorId(pacienteId:int):
    """Devuelve los encuentros cuya id de paciente coincida con la pasada"""

    req = requests.get(f"http://{host}:{port}/encuentros/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()
#Encuentros



#Medicaciones
@tool
def getAllMedicaciones():
    """Devuelve todas las medicaciones registradas."""

    req = requests.get(f"http://{host}:{port}/medicacion/")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getMedicacionPorId(pacienteId:int):
    """Devuelve las medicaciones cuya id de paciente coincida con la pasada"""

    req = requests.get(f"http://{host}:{port}/medicacion/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()
 #Medicaciones




#Procedimientos
@tool
def getAllProcedimientos():
    """Devuelve todos los procedimientos registradas."""

    req = requests.get(f"http://{host}:{port}/procedimientos/")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getProcedimientoPorId(pacienteId:int):
    """Devuelve los procedimientos cuya id de paciente coincida con la pasada"""

    req = requests.get(f"http://{host}:{port}/procedimientos/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()
#Procedimientos






#Alergias
@tool
def getAllAlergias():
    """Devuelve las alergias de todos los pacientes"""

    req = requests.get(f"http://{host}:{port}/alergias/")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()

@tool
def getAlergiasPaciente(pacienteId:int):
    """Devuelve las alergias de un paciente dado su id de paciente"""

    req = requests.get(f"http://{host}:{port}/alergias/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a {host}")
        return req.status_code

    return req.json()
#Alergias



tools = [getAlergiasPaciente,getAllAlergias,getAllPacientes, getPacientePorId, 
         getPacientePorProvincia, getAllCondiciones, getAllEncuentros, getAllMedicaciones, getAllProcedimientos,
         getProcedimientoPorId, getMedicacionPorId, getCondicionesPorId, getEncuentrosPorId]