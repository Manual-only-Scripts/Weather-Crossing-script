"""
Provides utilities for generating colored console text using RGB values or predefined color presets.

The `ConsolColor` class offers static methods for applying ANSI color codes to
text, enabling visually distinct console output. It supports both fully custom
RGB colors and a set of predefined semantic color types used throughout the
application to highlight tips, warnings, errors, and system messages.

Methods
-------
CustomColoredText(text: str, r: int, g: int, b: int) -> str:
    Returns the given text wrapped in ANSI escape codes that apply the specified
    RGB color. Useful for dynamic or custom color styling.

PreSetUpColoredTextLine(text: str, textType: str) -> str:
    Returns the text colored according to one of the predefined semantic color
    types. These presets are used to maintain consistent visual meaning across
    the application.

    Available textType values:
    - "ni_tips" — not‑important tips (black)
    - "i_tips" — important tips (light gray)
    - "s_color" — system default color (gray)
    - "is_color" — important system color (white)
    - "p_error" — possible error (yellow)
    - "warning" — warning (orange)
    - "danger" — danger (red)
    - "success" — success (green)
    - "info" — informational message (blue)

PreSetUpColorStart(textType: str) -> str:
    Returns only the ANSI start code for the given color preset. This is useful
    when constructing multi‑part colored messages manually.

PreSetUpColorEnd() -> str:
    Returns the ANSI reset code to end a colored text segment.

Behavior
--------
- All methods return strings containing ANSI escape sequences compatible with
    most terminals.
- Color presets ensure consistent styling across the application.
- The class is fully static and does not require instantiation.

Exports
-------
__all__ = ["ConsolColor"]
    Makes the color utility class available for import.
"""


from colorama import Style

class ConsolColor:
    @staticmethod
    def CustomColoredText(text : str, r : int, g : int, b : int) -> str:
        """
        Colors a given text to a given RGB color

        Args:
            szoveg (`str`): The text that you want to color.
            r (`int`): RGB color red.
            g (`int`): RGB color green.
            b (`int`): RGB color blue.

        Returns:
            `str`: Gives back the colored text.
        """
    
        color : str = f"\x1b[38;2;{r};{g};{b}m"
        coloredText : str = f"{color}{text}{Style.RESET_ALL}"
        return coloredText

    @staticmethod
    def PreSetUpColoredTextLine(text : str, textType : str) -> str:
        """
        Gives back a line of colored text with pre coded colors.

        Args:
            text (str): The text you want to color.
            textType (str): The color type.

        Returns:
            str: The colored text.

        ## Types
            `ni_tips` -> `not_important_tips` -> Tips that can be overlooked. It is a black color rgb(0,0,0).
            `i_tips` -> `important_tips` -> Tips that can make this process faster.
            `s_color` -> `system_color` -> The basic color that this code use.
            `is_color` -> `important_system_color` -> The system color that you sould look out for.
            `p_error` -> `possible_error` -> This colored message can lead to errors.
            `warning` -> `warning` -> This colored message is a warning.
            `danger` -> `danger` -> This colored message is a danger.
            `success` -> `success` -> This color means that the task went good.
            `info` -> `information` -> This colored message is an information.
        """

        Color : str = ""
        match textType:
            case "ni_tips":
                Color = f"\x1b[38;2;0;0;0m"
            case "i_tips":
                Color = f"\x1b[38;2;150;150;150m"
            case "s_color":
                Color = f"\x1b[38;2;200;200;200m"
            case "is_color":
                Color = f"\x1b[38;2;255;255;255m"
            case "p_error":
                Color = f"\x1b[38;2;255;230;0m"
            case "warning":
                Color = f"\x1b[38;2;255;100;0m [!!! WARNING !!!]"
            case "danger":
                Color = f"\x1b[38;2;255;0;0m [!!! DANGER !!!]"
            case "success":
                Color = f"\x1b[38;2;0;255;0m"
            case "info":
                Color = f"\x1b[38;2;0;0;255m"

        coloredText : str = f"{Color}{text}{Style.RESET_ALL}"
        return coloredText

    @staticmethod
    def PreSetUpColorStart(textType : str) -> str:
        """
        Gives back the start of colored line.

        Args:
            text (str): The text you want to color.
            textType (str): The color type.

        Returns:
            str: The colored text.

        ## Types
            `ni_tips` -> `not_important_tips` -> Tips that can be overlooked. It is a black color rgb(0,0,0).
            `i_tips` -> `important_tips` -> Tips that can make this process faster.
            `s_color` -> `system_color` -> The basic color that this code use.
            `is_color` -> `important_system_color` -> The system color that you sould look out for.
            `p_error` -> `possible_error` -> This colored message can lead to errors.
            `warning` -> `warning` -> This colored message is a warning.
            `danger` -> `danger` -> This colored message is a danger.
            `info` -> `information` -> This colored message is an information.
        """
    
        Color: str = ""
        match textType:
            case "ni_tips":
                Color = f"\x1b[38;2;0;0;0m"
            case "i_tips":
                Color = f"\x1b[38;2;150;150;150m"
            case "s_color":
                Color = f"\x1b[38;2;200;200;200m"
            case "is_color":
                Color = f"\x1b[38;2;255;255;255m"
            case "p_error":
                Color = f"\x1b[38;2;255;230;0m"
            case "warning":
                Color = f"\x1b[38;2;255;100;0m [!!! WARNING !!!]"
            case "danger":
                Color = f"\x1b[38;2;255;0;0m [!!! DANGER !!!]"
            case "info":
                Color = f"\x1b[38;2;0;0;255m"

        finalColor : str = f"{Color}"
        return finalColor

    @staticmethod
    def PreSetUpColorEnd() -> str:
        """
        Gives back the end of colored line.

        Returns:
            str: The end of colored text.
        """
        finalColorEnd = f"{Style.RESET_ALL}"
        return finalColorEnd   

__all__= ["ConsolColor"]