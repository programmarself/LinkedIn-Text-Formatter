﻿import streamlit as st

# Function to apply unicode formatting
def apply_unicode_formatting(text, bold, italic, strikethrough, monospace, superscript, subscript, uppercase, lowercase, titlecase, reverse):
    if bold:
        text = ''.join([chr(ord('𝐀') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝐚') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if italic:
        text = ''.join([chr(ord('𝑨') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝒂') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if strikethrough:
        text = ''.join([c + '\u0336' for c in text])
    if monospace:
        text = ''.join([chr(ord('𝙰') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝚊') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if superscript:
        superscript_map = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴽᴿˢᵀᵁⱽᵂ⁺⁻⁼⁽⁾')
        text = text.translate(superscript_map)
    if subscript:
        subscript_map = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', '₀₁₂₃₄₅₆₇₈₉ₐᵦᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓₓᵧₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓ
