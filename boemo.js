/**
 * This is a function.
 *
 * @param {string} n - A string param
 * @param {string} [o] - A optional string param
 *
 * @example
 */

}

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}
