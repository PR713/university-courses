actSeq = putChar 'A' >> putChar 'G' >> putChar 'H' >> putChar '\n'

doActSeq = do
	putChar 'A'
	putChar 'G'
	putChar 'H'
	putChar '\n'


echo1 = getLine >>= putStrLn

doEcho1 = do
	line <- getLine
	putStrLn line


echo2 = getLine >>= \line -> putStrLn $ line ++ "!"

doEcho2 = do
	line <- getLine
	putStrLn $ line ++ "!"



-- wykonujemy akcję IO (getLine) i przekazujemy wynik do funkcji czyli argument l1 to wynik getLine więc l1 = getLine i to zwraca następną akcję...
echo3 :: IO ()
echo3 =  getLine >>= \l1 -> getLine >>= \l2 -> putStrLn $ l1 ++ l2

dialog :: IO ()
dialog = putStr "What is your happy number? "
         >> getLine
         >>= \n -> let num = read n :: Int in --binding między getLine a n: >>=
                   if num == 7
                   then putStrLn "Ah, lucky 7!"
                   else if odd num
                        then putStrLn "Odd number! That's most people's choice..."
                        else putStrLn "Hm, even number? Unusual!"



doEcho3 :: IO ()
doEcho3 = do 
	l1 <- getLine
	l2 <- getLine
	putStrLn $ l1 ++ l2


doDialog :: IO ()
doDialog = do
    putStrLn "What is your happy number?"
    n <- getLine --nie ma bindingu tzn >>= więc trzeba tak
    let num = read n :: Int
    if num == 7
        then putStrLn "Ah, lucky 7!"
        else if odd num
            then putStrLn "Odd number! That's most people's choice..."
            else putStrLn "Hm, even number? Unusual!"



twoQuestions :: IO ()
twoQuestions = do
  putStr "What is your name? "
  name <- getLine
  putStr "How old are you? "
  age <- getLine
  print (name,age)
-- <- to złożony operator, pakujemy w kapsułę nieczystości jako akcję (np getLine to akcja IO) i potem to wyciągamy
-- lub np a <- return "a" 

casualTwoQuestions :: IO ()
casualTwoQuestions = putStr "What is your name? " >> getLine >>= \name -> putStr "How old are you? " >> getLine >>= \age -> print(name, age)


--improved 
casualTwoQuestionsImproved :: IO ()
casualTwoQuestionsImproved = putStr "What is your name? " >> getLine >>= \name -> putStr "How old are you? " >> getLine >>= \ageInput -> let age = read ageInput :: Int in print(name, age) -- nie można /nameInput -> let name = read... String >> bo let nie jest operacją monadyczną, defaultowo getLine zwraca string


--np getLine' :: IO String przyjmuje na wejściu stan maszyny (świata) i na wyjściu zwraca nowy stan świata i String
