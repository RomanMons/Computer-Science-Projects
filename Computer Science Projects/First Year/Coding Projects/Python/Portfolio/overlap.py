start_a = int(input("Enter start hour for event A: "))
dur_a = int(input("Enter duration of event A (in hours): "))
end_a = start_a+dur_a
start_b = int(input("Enter start hour for event B: "))
dur_b = int(input("Enter duration of event B (in hours): "))
end_b = start_b+dur_b
if start_a < start_b < end_a or start_a < end_b < end_a:
    print("Events overlap")
elif start_b < start_a < end_b or start_b < end_a < end_b:
    print("Events overlap")
else:
    print("Events do not overlap")
