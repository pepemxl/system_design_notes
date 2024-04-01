Para crear un smart contract en Ethereum, seguiremos los siguientes pasos:

1. Configuramos un entorno de desarrollo, instalaremos:
    - Node.js, 
    - npm (Node Package Manager) y 
    - un editor de texto o un IDE.

2. Crearremos un nuevo proyecto, para esto, abriremos una terminal y crearemos un nuevo directorio para el proyecto. Navega hasta el directorio y ejecuta el siguiente comando para inicializar un nuevo proyecto de npm:

   ```bash
   npm init
   ```

3. Instalaremos las dependencias necesarias, y entonces a continuación, instalaremos las dependencias necesarias para desarrollar smart contracts en Ethereum. Para esto, necesitarás instalar **Truffle** y **Ganache**, que son dos herramientas populares en el desarrollo de Ethereum. Ejecutaremos los siguientes comandos en la terminal:

   ```bash
   npm install -g truffle
   npm install -g ganache-cli
   ```

4. Configura el entorno de desarrollo local: Inicia Ganache para crear una red de desarrollo local Ethereum. Puedes ejecutar el siguiente comando en tu terminal:

   ```
   ganache-cli
   ```

   Esto iniciará una instancia local de Ethereum con cuentas pregeneradas para usar en tu desarrollo.

5. Crea un contrato inteligente: Ahora puedes crear tu contrato inteligente en un archivo de Solidity con extensión ".sol". Utiliza un editor de texto o un IDE para crear un nuevo archivo y escribe el código del contrato.

   Por ejemplo, puedes crear un contrato simple que almacene y recupere un valor entero:

   ```solidity
   pragma solidity ^0.8.0;

   contract MyContract {
       uint public myValue;

       function setValue(uint _value) public {
           myValue = _value;
       }

       function getValue() public view returns (uint) {
           return myValue;
       }
   }
   ```

6. Compila y migra el contrato: Usa Truffle para compilar y migrar tu contrato a la red local. En tu terminal, navega hasta el directorio de tu proyecto y ejecuta los siguientes comandos:

   ```
   truffle compile
   truffle migrate
   ```

   Esto compilará tu contrato y migrará el bytecode y la dirección a la red local de Ethereum.

7. Interactúa con el contrato: Ahora que tu contrato está desplegado en la red local, puedes interactuar con él. Puedes crear una interfaz de usuario o utilizar la consola de Truffle para interactuar con las funciones del contrato.

Estos son los pasos básicos para crear un smart contract en Ethereum. Recuerda que el desarrollo de contratos inteligentes implica una comprensión profunda de los conceptos de Ethereum y Solidity, así como buenas prácticas de seguridad. Es recomendable estudiar y familiarizarse con la documentación oficial de Ethereum y Solidity, así como explorar ejemplos y tutoriales adicionales para profundizar en el desarrollo de smart contracts.