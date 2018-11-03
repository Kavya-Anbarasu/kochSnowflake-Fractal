from turtle import *
bob = Turtle()

def snowflake(level, steps, color):
	if level == 1:
		bob.color(color)
		bob.forward(steps)
	
	elif level > 1:
		snowflake(level - 1, steps / 3, color)
		bob.left(60)
		snowflake(level - 1, steps / 3, color)
		bob.right(120)
		snowflake(level - 1, steps / 3, color)
		bob.left(60)
		snowflake(level - 1, steps / 3, color)
		
def main():
	bob.speed(0)
	for x in range (0 , 3):	
		snowflake (5, 300, "blue")
		bob.right(120)
	bob.right(180)
	exitonclick()
	
main()