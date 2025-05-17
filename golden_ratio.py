from manim import *

class GoldenRatioVisualization(Scene):
    def construct(self):
        # Title
        title = Tex("The Golden Ratio ($\\phi$)")
        title.scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Initialize variables
        a, b = 1, 1
        phi = (1 + math.sqrt(5)) / 2
        
        # Create initial square
        square = Square(side_length=a, color=BLUE)
        square.move_to(ORIGIN)
        self.play(Create(square))
        
        # Animation loop
        for i in range(6):
            # Add new square
            new_square = Square(side_length=b, color=BLUE)
            if i % 4 == 0:  # Right
                new_square.next_to(square, RIGHT, buff=0)
            elif i % 4 == 1:  # Top
                new_square.next_to(square, UP, buff=0)
            elif i % 4 == 2:  # Left
                new_square.next_to(square, LEFT, buff=0)
            else:  # Bottom
                new_square.next_to(square, DOWN, buff=0)
            
            self.play(Create(new_square))
            square = VGroup(square, new_square)
            
            # Draw the arc
            arc = Arc(
                radius=b,
                angle=90 * DEGREES,
                start_angle=(90 * i) * DEGREES,
                color=GOLD
            )
            self.play(Create(arc))
            
            # Update Fibonacci sequence
            a, b = b, a + b
        
        # Show the golden ratio value
        phi_text = MathTex("\\phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.618", color=YELLOW)
        phi_text.scale(1.5)
        phi_text.to_edge(DOWN)
        self.play(Write(phi_text))
        self.wait(3)
        
        # Explain the ratio
        explanation = Tex("Each new square's side is the sum of the previous two")
        explanation.next_to(phi_text, UP)
        self.play(Write(explanation))
        self.wait(3)

class GoldenRatioSpiral(Scene):
    def construct(self):
        # More advanced spiral visualization
        pass
