sqr :: Double -> Double
sqr x = x * x

vec2Dlen :: (Double, Double) -> Double
vec2Dlen (x,y) = sqrt(x^2 + y^2)

vec3DLen :: (Double, Double, Double) -> Double
vec3DLen (x,y,z) = sqrt (x^2 + y^2 + z^2)

swap :: (Int, Char) -> (Char, Int)
swap (x,y) = (y,x)

threeEqual :: (Int, Int, Int) -> Bool
threeEqual (x, y, z) = if x == y && y == z then True else False
--lub (x,y,z) = x==y && y == z

heron :: (Double, Double, Double) -> Double
heron (a, b, c) = sqrt (((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))
--z where można s = (a+b+c)/2