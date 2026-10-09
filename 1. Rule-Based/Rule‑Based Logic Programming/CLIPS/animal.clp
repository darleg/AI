(defrule identify-animal
  (animal-is ?type)
  =>
  (printout t "The animal is a " ?type "." crlf))
(defrule ask-animal
  =>
  (printout t "What type of animal is it? (e.g., mammal, bird, reptile): " crlf)
  (bind ?type (read))
  (assert (animal-is ?type)))
(defrule mammal-characteristics
  (animal-is mammal)
  =>
  (printout t "Mammals are warm-blooded and have fur or hair." crlf))
(defrule bird-characteristics
  (animal-is bird)
  =>
  (printout t "Birds have feathers and lay eggs." crlf))
(defrule reptile-characteristics
  (animal-is reptile)
  =>
  (printout t "Reptiles are cold-blooded and have scales." crlf))
(defrule unknown-animal
  (animal-is ?type)
  (not (or (eq ?type mammal) (eq ?type bird) (eq ?type reptile)))
  =>
  (printout t "Sorry, I don't have information about " ?type "." crlf))
(reset)
(run)