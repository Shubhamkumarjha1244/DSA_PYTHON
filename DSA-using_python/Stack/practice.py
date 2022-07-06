class A:
	x=10
	pass
class B(A):
	#x=2
	pass
class C:
	pass
class D:
	x=9
	pass
class F(D):
	x=5
	pass
class E(B,C,F):
	pass

c=E()
print(c.x)

