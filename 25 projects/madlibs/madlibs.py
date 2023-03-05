from create import createMadlibs, solve

text = "Con un rotulador borrable, haz un dibujo sencillo en el plato o recipiente de vidrio. Por ejemplo, una figura de palo, corazones o estrellas. Lentamente, vierte un poco de agua en el plato o en el recipiente de vidrio para levantar el dibujo del plato. Por último, agita el plato para hacer que el dibujo se mueva y observa con detenimiento lo que sucede."

m1 = createMadlibs(text, 4)
solve(m1)
