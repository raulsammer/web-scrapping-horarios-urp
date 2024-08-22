import datetime
import pandas as pd
import json
import re

# Leer el CSV
df = pd.read_csv('tabla.csv')

# Estructura de datos para almacenar el JSON final
json_data = {"carreras": []}

# Iterar sobre cada fila del DataFrame
for _, row in df.iterrows():
    carrera_existente = next((carrera for carrera in json_data["carreras"] if carrera["nombre"] == row["Carrera"]), None)

    if carrera_existente:
        malla_existente = next((malla for malla in carrera_existente["mallas_curriculares"] if malla["nombre"] == row["Malla"]), None)

        if malla_existente:
            semestre_existente = next((semestre for semestre in malla_existente["semestres"] if semestre["numero"] == row["Semestre"]), None)

            if semestre_existente:
                curso_existente = next((curso for curso in semestre_existente["cursos"] if curso["id"] == row["Curso"]), None)

                if curso_existente:
                    grupo_existente = next((grupo for grupo in curso_existente["grupos"] if grupo["id"] == row["Grp"]), None)

                    if grupo_existente:
                        subgrupo = int(re.search(r'\d+', row["SGrp"]).group())
                        horas_str = str(row["Horario"])  # Asegurar que sea una cadena
                        start_hour, start_minute, end_hour, end_minute = map(int, re.findall(r'\d+', horas_str))
                        start_time = f"{datetime.datetime.now().year}-01-01T{start_hour:02d}:{start_minute:02d}:00"
                        end_time = f"{datetime.datetime.now().year}-01-01T{end_hour:02d}:{end_minute:02d}:00"

                        grupo_existente["horarios"].append({
                            "tipo": row["Tipo"],
                            "dia": row["Dia"],
                            "start": start_time,
                            "end": end_time,
                            "profesor": row["Docente"],
                            "subgrupo": subgrupo
                        })
                    else:
                        subgrupo = int(re.search(r'\d+', row["SGrp"]).group())
                        horas_str = str(row["Horario"])  # Asegurar que sea una cadena
                        start_hour, start_minute, end_hour, end_minute = map(int, re.findall(r'\d+', horas_str))
                        start_time = f"{datetime.datetime.now().year}-01-01T{start_hour:02d}:{start_minute:02d}:00"
                        end_time = f"{datetime.datetime.now().year}-01-01T{end_hour:02d}:{end_minute:02d}:00"

                        curso_existente["grupos"].append({
                            "id": row["Grp"],
                            "horarios": [{
                                "tipo": row["Tipo"],
                                "dia": row["Dia"],
                                "start": start_time,
                                "end": end_time,
                                "profesor": row["Docente"],
                                "subgrupo": subgrupo
                            }]
                        })
                else:
                    curso_id = re.sub(r'\s', '', row['Curso'])

                    subgrupo = int(re.search(r'\d+', row["SGrp"]).group())
                    horas_str = str(row["Horario"])  # Asegurar que sea una cadena
                    start_hour, start_minute, end_hour, end_minute = map(int, re.findall(r'\d+', horas_str))
                    start_time = f"{datetime.datetime.now().year}-01-01T{start_hour:02d}:{start_minute:02d}:00"
                    end_time = f"{datetime.datetime.now().year}-01-01T{end_hour:02d}:{end_minute:02d}:00"

                    semestre_existente["cursos"].append({
                        "id": f"CU-{curso_id}",
                        "title": row["Curso"],
                        "grupos": [{
                            "id": row["Grp"],
                            "horarios": [{
                                "tipo": row["Tipo"],
                                "dia": row["Dia"],
                                "start": start_time,
                                "end": end_time,
                                "profesor": row["Docente"],
                                "subgrupo": subgrupo
                            }]
                        }]
                    })
            else:
                curso_id = re.sub(r'\s', '', row['Curso'])
                subgrupo = int(re.search(r'\d+', row["SGrp"]).group())
                horas_str = str(row["Horario"])  # Asegurar que sea una cadena
                start_hour, start_minute, end_hour, end_minute = map(int, re.findall(r'\d+', horas_str))
                start_time = f"{datetime.datetime.now().year}-01-01T{start_hour:02d}:{start_minute:02d}:00"
                end_time = f"{datetime.datetime.now().year}-01-01T{end_hour:02d}:{end_minute:02d}:00"

                malla_existente["semestres"].append({
                    "numero": row["Semestre"],
                    "cursos": [{
                        "id": f"CU-{curso_id}",
                        "title": row["Curso"],
                        "grupos": [{
                            "id": row["Grp"],
                            "horarios": [{
                                "tipo": row["Tipo"],
                                "dia": row["Dia"],
                                "start": start_time,
                                "end": end_time,
                                "profesor": row["Docente"],
                                "subgrupo": subgrupo
                            }]
                        }]
                    }]
                })
        else:
            curso_id = re.sub(r'\s', '', row['Curso'])
            subgrupo = int(re.search(r'\d+', row["SGrp"]).group())
            horas_str = str(row["Horario"])  # Asegurar que sea una cadena
            start_hour, start_minute, end_hour, end_minute = map(int, re.findall(r'\d+', horas_str))
            start_time = f"{datetime.datetime.now().year}-01-01T{start_hour:02d}:{start_minute:02d}:00"
            end_time = f"{datetime.datetime.now().year}-01-01T{end_hour:02d}:{end_minute:02d}:00"

            carrera_existente["mallas_curriculares"].append({
                "nombre": row["Malla"],
                "semestres": [{
                    "numero": row["Semestre"],
                    "cursos": [{
                        "id": f"CU-{curso_id}",
                        "title": row["Curso"],
                        "grupos": [{
                            "id": row["Grp"],
                            "horarios": [{
                                "tipo": row["Tipo"],
                                "dia": row["Dia"],
                                "start": start_time,
                                "end": end_time,
                                "profesor": row["Docente"],
                                "subgrupo": subgrupo
                            }]
                        }]
                    }]
                }]
            })
    else:
        curso_id = re.sub(r'\s', '', row['Curso'])
        subgrupo = int(re.search(r'\d+', row["SGrp"]).group())
        horas_str = str(row["Horario"])  # Asegurar que sea una cadena
        start_hour, start_minute, end_hour, end_minute = map(int, re.findall(r'\d+', horas_str))
        start_time = f"{datetime.datetime.now().year}-01-01T{start_hour:02d}:{start_minute:02d}:00"
        end_time = f"{datetime.datetime.now().year}-01-01T{end_hour:02d}:{end_minute:02d}:00"

        json_data["carreras"].append({
            "nombre": row["Carrera"],
            "mallas_curriculares": [{
                "nombre": row["Malla"],
                "semestres": [{
                    "numero": row["Semestre"],
                    "cursos": [{
                        "id": f"CU-{curso_id}",
                        "title": row["Curso"],
                        "grupos": [{
                            "id": row["Grp"],
                            "horarios": [{
                                "tipo": row["Tipo"],
                                "dia": row["Dia"],
                                "start": start_time,
                                "end": end_time,
                                "profesor": row["Docente"],
                                "subgrupo": subgrupo
                            }]
                        }]
                    }]
                }]
            }]
        })

# Guardar el resultado en un archivo JSON
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print("Proceso completado. El JSON ha sido generado.")
