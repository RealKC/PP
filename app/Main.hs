module Main where

import System.IO

removePunctuation :: String -> String
removePunctuation = filter (`notElem` ".,?!-_:;/()'\"")

main :: IO ()
main = do
  putStr "Introduce numele fisierului pentru a fi procesat: "
  hFlush stdout
  filePath <- getLine
  contents <- readFile filePath
  putStr (removePunctuation contents)
