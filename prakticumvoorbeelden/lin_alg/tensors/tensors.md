# TINLABML Lineaire Algebra 

## Tensors

**Exercise 1**
<p>
Voeg de volgende relaties toe aan onderstaand Class Diagram
<ol>
<li>Scalar <i>is a</i> Tensor</li>
<li>Vector <i>is a</i> Tensor</li>
<li>Matrix <i>is a</i> Tensor</li>
<li>Scalar <i>is a</i> Float</li>
<li>Vector <i>is a</i> Tuple</li>
<li>Matrix <i>is a</i> List</li>
<li>Vector <i>is composed by</i> Scalar</li>
<li>Matrix <i>is composed by</i> Vector</li>
</ol>
</p>
<note>

Zie [Mermaid Class diagrams](https://mermaid.js.org/syntax/classDiagram.html) voor de Markdown syntax

</note>

```mermaid
classDiagram
    Tensor <|-- Scalar : 1 Inheritance
    Tensor <|-- Vector : 2
    Tensor <|-- Matrix : 3


    class Tensor {
        -dimensions: tuple 
        +init()
        +add(Tensor other) 
        +mult(Tensor other)
        +getDimensions(): tuple
        +str(): str
    }

    class Scalar {
        +init()
        +add(Scalar other): Scalar
        +mult(Scalar other): Scalar
        +float(): float
    }

    class Vector {
        +init()
        +add(Vector other): Vector
        +mult(Tensor other): Scalar
        +list()
    }

    class Matrix {
        +init()
        +add(Matrix other): Matrix
        +mult(Tensor other): Tensor
        +getColumn(index): Vector
        +getRow(index): Vector
    }
```
<br>

**Exercise 2**
<p>
<ol>
<li>
Zorg ervoor dat er voor elke method uit tensors.py een unit test is in de test modules.
</li>
<li>
Vul de Classes in module tensors.py aan zodat alle methods geimplementeerd zijn zodanig dat alle unit tests slagen. 
</li>
<li>
Implementeer het vermenigvuldigen van een Scalar met een Vector in Class Scalar.
</li>
<li>
Implementeer het vermenigvuldigen van een Matrix met een Vector in Class Matrix.
</li>
</ol>
</p>