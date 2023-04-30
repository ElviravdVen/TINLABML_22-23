```mermaid
classDiagram
    class Figure {
       -shape: Numpy Array
        +init(shape, color)
        +getColor(): str
        +getShape(): Numpy Array 
        +rotate()
    }
```