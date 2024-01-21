# Code ownership

Según algunos autores, existen algunos casos de propiedad del código, tres que consideraríamos son:


- **Strong code ownership**  divide una base de código en módulos, clases, funciones, archivos y asigna cada módulo a un desarrollador. Los desarrolladores sólo pueden realizar cambios en los módulos de su propiedad. Si necesitan realizar un cambio en el módulo de otra persona, deben hablar con el propietario del módulo y pedirle que realice el cambio. Puede acelerar este proceso escribiendo un parche para el otro módulo y enviarlo al dueño del modulo, que es como comúnmente ocurre con los proyectos públicos en github.
- **Weak code ownership** es similar en que los módulos se asignan a los propietarios, pero se diferencia en que los desarrolladores pueden cambiar los módulos que pertenecen a otras personas. Se espera que los propietarios de los módulos asuman la responsabilidad de los módulos que poseen y estén atentos a los cambios realizados por otras personas. Si desea realizar un cambio sustancial en el módulo de otra persona.
- **Collective code ownership** abandona cualquier noción de propiedad individual de los módulos. El código base es propiedad de todo el equipo y cualquiera puede realizar cambios en cualquier lugar. Puede considerar esto como una ausencia de propiedad del código, pero sus defensores prefieren el énfasis en la noción de propiedad por parte de un equipo en lugar de un individuo. (El término propiedad colectiva del código proviene de Extreme Programming, aunque en la segunda edición la práctica se llama Código Compartido).

