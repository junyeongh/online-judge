-- $ nix-shell -p ghc --run "runghc main.hs"

-- 1
import Data.List (intercalate)

josephus :: Int -> Int -> [Int]
josephus n k = go [1..n]
  where
    go [] = []
    go xs =
      let idx = (k - 1) `mod` length xs
          (a, e:b) = splitAt idx xs
      in e : go (b ++ a)

main :: IO ()
main = do
  [n, k] <- map read . words <$> getLine
  let result = josephus n k
  putStrLn $ "<" ++ intercalate ", " (map show result) ++ ">"

-- 2
import Data.Sequence (Seq, ViewL(..), (><), viewl)
import qualified Data.Sequence as Seq
import Data.List (intercalate)

josephus :: Int -> Int -> [Int]
josephus n k = go (Seq.fromList [1..n])
  where
    go xs
      | Seq.null xs = []
      | otherwise =
          let idx       = (k - 1) `mod` Seq.length xs -- O(1)
              (a, rest) = Seq.splitAt idx xs          -- O(log n)
          in case viewl rest of
              e :< b -> e : go (b >< a)              -- >< is O(log n)
              EmptyL -> []

main :: IO ()
main = do
  [n, k] <- map read . words <$> getLine
  putStrLn $ "<" ++ intercalate ", " (map show (josephus n k)) ++ ">"
