"""the painful calculator of infection spread, basically coronavirus."""
__author__ = "730321206"

r0: float = input("Enter R0:")
t0: float = input("Enter t0 Cluster Size:")
r1: int = (round(float(r0) * float(t0)))
t1: int = (round(float(r1) + float(t0)))
t1stringnew: str = "t1 - New: "
t1stringtotal: str = " - Total: "
print(t1stringnew + str(r1) + t1stringtotal + str(t1))
r2: int = (round(float(r1) * float(r0)))
t2: int = (round(float(r2) + float(t1)))
t2stringnew: str = "t2 - New: "
t2stringtotal: str = " - Total: "
print(t2stringnew + str(r2) + t2stringtotal + str(t2))
r3: int = (round(float(r2) * float(r0)))
t3: int = (round(float(r3) + float(t2)))
t3stringnew: str = "t3 - New: "
t3stringtotal: str = " - Total: "
print(t3stringnew + str(r3) + t3stringtotal + str(t3))
r4: int = (round(float(r3) * float(r0)))
t4: int = (round(float(r4) + float(t3)))
t4stringnew: str = "t4 - New: "
t4stringtotal: str = " - Total: "
print(t4stringnew + str(r4) + t4stringtotal + str(t4))