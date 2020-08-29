%Ejercicio 1(TP n°2)
%Rama izquierda
verificar(thikness):-   (estado(thikness,T), (T>Tlimit; T=Tlimit), writeln('La condición del equipamiento es adecuado').
verificar(thikness):-   (estado(thikness,T), (T<Tlimit), writeln('El estado del equipamiento será reportado').
verificar(thikness):-   (estado(thikness,T), (T,desconocido)),( (estado(dazzling_rusting,no), writeln('Diamatro desconocido'));
                                                                verificar(dazzling_rusting)).

verificar(dazzling_rusting):-   estado(dazzling_rusting, desconocido), writeln('Verificar válvulas de seguridad, tubos y juntas').
verificar(dazzling_rusting):-   estado(dazzling_rusting, si), writeln('Se requiere coordinación para colorear y renderizar el equipo').
verificar(dazzling_rusting):-   estado(dazzling_rusting, no), writeln('Valvulas no oxidadas').

%Rama central
verificar(pilot) :-    estado(pilot, si), estado(leakage_prevention,si), writeln('Colocar la válcula de seguridad siguiendo las instrucciones').
verificar(pilot) :-    estado(pilot, no), estado(leakage_prevention,si), writeln('Full service y reinstalación del Piloto necesarios').
verificar(pilot) :-    estado(pilot, desconocido), 
                        ((estado(leakage_prevention, si), writeln('Verificar Piloto'));
                        verificar(leakage_prevention)).

verificar(leakage_prevention) :- 
                estado(leakage_prevention, desconocido), 
                ((estado(valve_spring, si), writeln('Verificar leakage prevention between sit and orifice')); 
                verificar(valve_spring)).
verificar(leakage_prevention) :-    estado(leakage_prevention, si), estado(valve_spring, si).
verificar(leakage_prevention) :-    estado(leakage_prevention, no), estado(valve_spring, si), writeln('Replace sit and orifice and put the safety valve on circuit').               

verificar(valve_spring) :-          estado(valve_spring, desconocido), 
                                    ((estado(control_valve_sensors_blocked, no), writeln('Verificar safety valve spring')); 
                                    verificar(control_valve_sensors_blocked)).
verificar(valve_spring) :-          estado(valve_spring, si), estado(control_valve_sensors_blocked, no).
verificar(valve_spring) :-          estado(valve_spring, no), estado(control_valve_sensors_blocked, no), writeln('Poner en servicio').

verificar(control_valve_sensors_blocked) :-         
                estado(control_valve_sensors_blocked, desconocido), 
                ((estado(valve_status_closed, no), writeln('Verificar control valve sensors blocked')); 
                verificar(valve_status_closed)).
verificar(control_valve_sensors_blocked) :-     estado(control_valve_sensors_blocked, si), estado(valve_status_closed, no),
                                                writeln('Limpiar y solucionar problemas en sensing pipes').                 
verificar(control_valve_sensors_blocked) :-     estado(control_valve_sensors_blocked, no), estado(valve_status_closed, no).
                                                

verificar(valve_status_closed) :- 
                estado(valve_status_closed, desconocido),
                ((estado(relief_valve, no), writeln('Verificar valve status "Close"'));
                verificar(relief_valve)).
verificar(valve_status_closed) :-               estado(valve_status_closed, si), estado(relief_valve, no), 
                                                writeln('Poner la válvula de seguridad en OPEN').
verificar(valve_status_closed) :-               estado(valve_status_closed, no), estado(relief_valve, no).                                           

verificar(relief_valve) :-              estado(relief_valve, desconocido),
                                        ((estado(cont_gas_evacuation, no),
                                        writeln('Verificar si la valvula de seguridad funciona correctamente con +10% sobre la presión regular')); 
                                        verificar(cont_gas_evacuation)).
verificar(relief_valve) :-              estado(relief_valve, si), estado(cont_gas_evacuation,no), writeln('Funcion de seguridad: apropiado').         
verificar(relief_valve) :-              estado(relief_valve, no), estado(cont_gas_evacuation,no).         

verificar(cont_gas_evacuation) :- 
                estado(cont_gas_evacuation, desconocido), 
                writeln('Verificar safety valve has continuous evacuation').
verificar(cont_gas_evacuation) :-       estado(cont_gas_evacuation,si), writeln('Si').
verificar(cont_gas_evacuation) :-       estado(cont_gas_evacuation,no), writeln('No').

verificar(preventable_leakage):-        estado(preventable_leakage, desconocido),
                                        ((estado(safety_spring, si), writeln('Verificar si hay fuga prevenible'));
                                        verificar(safety_spring)).
verificar(preventable_leakage):-        estado(preventable_leakage,si), estado(safety_spring,si),
                                        writeln('Colocar la válvula de seguridad según instrucciones').
verificar(preventable_leakage):-        estado(preventable_leakage,no), estado(safety_spring,si),
                                        writeln('Replace sit and orifice and put the valve into circuit').

verificar(safety_spring):-              estado(safety_spring,desconocido),
                                        (estado(control_pressure_pipes_blocked,si), writeln('Verificar resortes de seguridad'));
                                        verificar(control_pressure_pipes_blocked).
verificar(safety_spring):-              estado(safety_spring,no), estado(control_pressure_pipes_blocked, no),
                                        writeln('Reemplazar el resorte de seguridad').
verificar(safety_spring):-              estado(safety_spring,si), estado(control_pressure_pipes_blocked, no).

verificar(control_pressure_pipes_blocked):- estado(control_pressure_pipes_blocked, desconocido),
                                            (estado(line_gas_pressure_appropiate,si), writeln('Verificar Pressure sensor pipes'));
                                            verificar(line_gas_pressure_appropiate).
verificar(control_pressure_pipes_blocked):- estado(control_pressure_pipes_blocked, si), estado(line_gas_pressure_appropiate,si),
                                            writeln('Limpiar y arreglar fallas de sensing pipes').
verificar(control_pressure_pipes_blocked):- estado(control_pressure_pipes_blocked, no), estado(line_gas_pressure_appropiate,si).


verificar(line_gas_pressure_appropiate):-   estado(line_gas_pressure_appropiate, desconocido),
                                            (estado(cont_gas_evacuation, si), writeln('Verificar presión de linea de gas'));
                                            verificar(cont_gas_evacuation).
verificar(line_gas_pressure_appropiate):-   estado(line_gas_pressure_appropiate, si), estado(cont_gas_evacuation, si).
verificar(line_gas_pressure_appropiate):-   estado(line_gas_pressure_appropiate, no), estado(cont_gas_evacuation, si),
                                            writeln('Ajustar el regulador según instrucciones').

%Rama derecha
verificar(leakage_fixed_with_wrench):-      estado(leakage_fixed_with_wrench, desconocido), (estado(leakage_at_joint,si),
                                            writeln('Verificar si se solucionaron las fugas'));
                                            verificar(leakage_at_joint).
verificar(leakage_fixed_with_wrench):-      estado(leakage_fixed_with_wrench, si), (estado(leakage_at_joint,si),
                                            writeln('Reportar a Unidad de Inspección Técnica').
verificar(leakage_fixed_with_wrench):-      estado(leakage_fixed_with_wrench, no), (estado(leakage_at_joint,si),
                                            writeln('Enviar reporte a el departamento de reparaciones').      

verificar(leakage_at_joint):-               estado(leakage_at_joint, desconocido), writeln('Verificar').
verificar(leakage_at_joint):-               estado(leakage_at_joint, si), writeln('Hay pérdidas').
verificar(leakage_at_joint):-               estado(leakage_at_joint, no), writeln('Sin perdidas en la junta').                                  
                                            


            


%No se si es punto y coma entre sentencias (si, no, desconocido) o van puntos (ver video de teoría)
%Ver si en vez de ir definiendo de a uno no se puede usar una OR con ;
%Tratar de agregar signo ! al final de las sentencias (probar), esto es para el corte.

%Base de conocimientos
Tlimit is 100.
estado(thikness, T), T is 50.
estado(dazzling_rusting, no).
estado(pilot, si).
estado(leakage_prevention, no).
estado(valve_spring, no).
estado(control_valve_sensors_blocked, si).
estado(valve_status_closed, no).
estado(relief_valve, desconocido).
estado(cont_gas_evacuation,no).
estado(preventable_leakage, desconocido).
estado(safety_spring, desconocido).
estado(control_pressure_pipes_blocked, no).
estado(line_gas_pressure_appropiate, si).
estado(leakage_fixed_with_wrench, desconocido).
estado(leakage_at_joint, si).
