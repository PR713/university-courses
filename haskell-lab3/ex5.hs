import Data.List (sort)

sortDesc :: Ord a => [a] -> [a]
sortDesc xs = reverse ( sort xs)


sortDesc1 :: Ord a => [a] -> [a]
sortDesc1 = reverse . sort
