from langchain.tools import tool
import os
import requests

port = os.getenv("DATAPOINT_PORT")

@tool
def getAllPacientes():
    """Devuelve los datos de todos los pacientes."""

    req = requests.get(f"http://127.0.0.1:{port}/pacientes/getAllPacientes")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()

@tool
def getPacientePorProvincia(provincia: str):
    """Devuelve los pacientes de una povincia"""

    req = requests.get(f"http://127.0.0.1:{port}/pacientes/getPacientePortProvincia/{provincia}")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()

@tool
def getPacientePorId(pacienteId:int):
    """Devuelve un paciente cuya id coincida con la pasada"""

    req = requests.get(f"http://127.0.0.1:{port}/pacientes/getPacientePorId/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()


@tool
def getAllCondiciones():
    """Devuelve todas las condiciones registradas."""

    req = requests.get(f"http://127.0.0.1:{port}/condiciones/getAllCondiciones")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()

@tool
def getAllEncuentros():
    """Devuelve todos los encuentros registradas."""

    req = requests.get(f"http://127.0.0.1:{port}/encuentros/getAllEncuentros")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()

@tool
def getAllMedicaciones():
    """Devuelve todas las medicaciones registradas."""

    req = requests.get(f"http://127.0.0.1:{port}/medicacion/getAllMedicaciones")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()

@tool
def getAllProcedimientos():
    """Devuelve todos los procedimientos registradas."""

    req = requests.get(f"http://127.0.0.1:{port}/procedimientos/getAllProcedimientos")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()



@tool
def getAllAlergias():
    """Devuelve las alergias de todos los pacientes"""

    req = requests.get(f"http://127.0.0.1:{port}/alergias/getAllAlergias")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()

@tool
def getAlergiasPaciente(pacienteId:int):
    """Devuelve las alergias de un paciente dado su id de paciente"""

    req = requests.get(f"http://127.0.0.1:{port}/alergias/getAlergiasPaciente/{pacienteId}")
    if req.status_code != 200:
        print("Error al pedir un dato a DataPoint")
        return req.status_code

    return req.json()




tools = [getAlergiasPaciente,getAllAlergias,getAllPacientes, getPacientePorId, 
         getPacientePorProvincia, getAllCondiciones, getAllEncuentros, getAllMedicaciones, getAllProcedimientos]