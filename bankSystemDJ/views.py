from django.shortcuts import render
from bankSystemDJ.cuenta          import Cuenta


def home(request):
    v_idOwner = 2020  # Francisco
    return render(request,'home.html',{'idOwner':v_idOwner})

def transferencia(request,p_idOwner):

    #Se CREA un objeto CUENTA
    obj_cuenta = Cuenta(p_idOwner)

    # Cuando se lanza el formulario
    if (request.method == 'GET'):

                # Trae el nombre del cliente
                obj_cuenta.getName()
                # Trae las cuentas inscritas
                obj_cuenta.getInscritas()
                obj_cuenta.closeBD()

                return render('transferencia.html',{'balance':obj_cuenta.balance,'idCuenta':obj_cuenta.idCue,'idOwner':obj_cuenta.p_idOwner,'nameOwner':obj_cuenta.nameOwner,'inscritas':obj_cuenta.inscritas})

    else:
            #Cuando el metodo es POST
            try:
                 # Obtenemos la cuenta destino del formulario
                 v_cueDestino = request.form.get('enti')

                 #Obtenemos el valor a transferir y validamos tambien que no se violen las restricciones
                 v_valor      = request.form.get('valorTran')

                 if int(v_valor) > int(obj_cuenta.balance):
                     obj_cuenta.closeDB()
                     return render('alarmaErrorValor.html')
                 else:

                    obj_cuenta.transferencia(v_valor,v_cueDestino)
                    obj_cuenta.closeDB()
                    return render('alarma.html')

            except:
                 obj_cuenta.closeDB()
                 return render('home.html')
