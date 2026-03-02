;;; Homework 08: Scheme

;;; Required Problems

(define (square x) (* x x))

;; Problem 1: Quick Pow

(define (quick-pow base exp)
	(if (= exp 0) 1 
			(if (= exp 1) base 
			(if (= exp 2) (square base)
				(if (even? exp) 
					(quick-pow (square base) (/ exp 2))
					(* base (quick-pow (square base) (/ (- exp 1) 2)))
					)
				)
			)
		)
)

;; Problem 2: Quicker Pow

(define (quicker-pow base exp)
  (if (= exp 0) 1 
			(if (= exp 1) base 
			(if (= exp 2) (square base)
				(if (even? exp) 
					(quick-pow (square base) (/ exp 2))
					(* base (quick-pow (square base) (/ (- exp 1) 2)))
					)
				)
			)
		)
)

;; Problem 3: Find

(define (find predicate lst)
	(if (null? lst)	
		#f
		(if (null? (cdr lst))
			(if (predicate (car lst)) 
				(car lst)
				#f)
			(if (predicate (car lst)) 
				(car lst)
				(find predicate (cdr lst))))
		)
)

;; Problem 4: Count Change III

(define (make-change total biggest)
  (if (= total 0)
      '(())
      (if (or (< total 0) (= biggest 0))
          '()
          (append
            (map (lambda (rest) (cons biggest rest))
                 (make-change (- total biggest) biggest))
            (make-change total (- biggest 1))
          )
      )
  )
)

;; Problem 5: Enumerate

(define (enumerate lst)
	(define (enumerate-tail lst res count)
		(if (null? lst)
			res
			(enumerate-tail (cdr lst) (append res (list(cons count (car lst)))) (+ count 1)))
	)
(enumerate-tail lst () 0)
)

;; Problem 6: Substitute

(define (substitute bindings s)
  (cond ((null? s) nil)
        ((pair? s) (cons (substitute bindings (car s))
                         (substitute bindings (cdr s))))
        (else (let ((b (find (lambda (x) (equal? (car x) s)) bindings)))
                (if b (cdr b) s)))))

;; Problem 7: Tree in Scheme

(define (tree label branches)
  (cons label branches)
)

(define (label t)
  (car t)
)

(define (branches t)
  (cdr t)
)

(define (is-leaf t)
  (null? (branches t))
)

; A tree for test
(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
        (tree 6 (list
          (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))




;; Problem 8: Label Sum

(define (label-sum t)
	(define (helper res lst)
		(if (null? lst)
			res
			(if (is-leaf (car lst)) 
				(helper (+ res (label (car lst))) (cdr lst))
				(+ (label-sum (car lst)) (helper res (cdr lst)))
				)
			)
		)
	(if (null? t)
		0
		(if (is-leaf t) 
			(label t)
			(helper (label t) (branches t)))
	)
)


;;; Just For Fun Problems

;; Problem 9: Derive

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand (already defined for sum).
; (define (first-operand p) (cadr p))
; (define (second-operand p) (caddr p))

;; Problem 9.1: Derive Sum

(define (derive-sum expr var)
  'YOUR-CODE-HERE
)

;; Problem 9.2: Derive Product

(define (derive-product expr var)
  'YOUR-CODE-HERE
)

;; Problem 9.3: Make Exp

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  'YOUR-CODE-HERE
)

(define (exp? exp)
  'YOUR-CODE-HERE
)

; Some expressions for test
(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

;; Problem 9.4: Derive Exp

(define (derive-exp exp var)
  'YOUR-CODE-HERE
)


