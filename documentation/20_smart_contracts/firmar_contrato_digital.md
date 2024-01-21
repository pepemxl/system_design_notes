# Firmar un contrato en Blockchain

Para firmar un contrato digital utilizando MetaMask y la red Ethereum:

- Configuramos MetaMask: Instalamos la extensión(si no la tenemos ya instalada) de MetaMask en el navegador y configuramos la billetera Ethereum.

- Preparamos el contrato: Preparamos el código del contrato digital que deseamos firmar. Esto implica tener el código fuente del contrato y la información necesaria para su despliegue, esto es:
    - Código fuente del contrato: Debemos tener el código fuente del contrato que deseamos desplegar/lanzar.
    - Compilación del contrato: El código fuente del contrato debe ser compilado en bytecode ejecutable a esto es lo que le llamamos el binario. Las herramientas clásicas para compilar contratos parecen ser Remix y/o Truffle.

    - Parámetros de configuración: Al desplegar un contrato, es posible que se requieran ciertos parámetros de configuración, como valores iniciales para variables internas del contrato o direcciones de contratos relacionados. 

- Despliega el contrato: Las herramientas clásicas son Remix o Truffle, para compilar y desplegar el contrato en la red Ethereum. Aquí se genera el hash del contrato!

- Confirma la transacción: MetaMask nos mostrará los detalles de la transacción generada durante el despliegue del contrato. Debe asegurarse de revisar y aceptar los costos asociados con la transacción, como las comisiones de gas.

- Firmar la transacción: Una vez que la transacción esté confirmada, MetaMask te pedirá que firmes la transacción digitalmente utilizando tu clave privada.(aquí firmar significa autorizar usando tu clave privada de la billetera)