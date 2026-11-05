# B02 permanent signal connection board

PHASE 1: MATERIALS BUYING, Step 51 — 16 October 2026.

B02 makes the controller's low-current signal connections more secure for the permanent machine. A screw terminal grips a wire under a screw rather than relying on a loose jumper connection. A shield is a board designed to plug into a controller's headers. The controller remains A01; this is not a second Arduino.

## First listing to compare

Search `Arduino Mega 2560 R3 screw terminal shield` or `Mega 2560 terminal block expansion board`.

Compare quantity one, compatible with the **full-size Mega 2560 R3** selected in A01. Verify pin coverage/labels, header alignment and clearance, whether header pins/terminals are supplied already soldered, accessible USB/reset, and low-voltage power routing. The connector board does not add motor current capacity to Arduino pins.

[DFRobot's Mega terminal shield](https://www.dfrobot.com/product-2574.html) is a manufacturer example of this category, not a selected PH supplier or price. Do not assume another generic listing shares its exact features or ratings.

An assembled suitable screw-terminal board can reduce the custom interconnect soldering needed. It does not remove the need for secure wire preparation, mounting or checking every connection. Keep driver power and any mains connections off this signal board.

## Economical alternative if the shield costs too much

Search `FR4 double sided prototype PCB 2.54mm perfboard` for a solder board with individual plated pads. A roughly 7×9 cm board is a size to compare, not a validated layout. Confirm actual board size after arranging the required low-voltage signal parts. Header strips and suitable terminals would be needed; reuse A14 terminals where suitable and do not buy duplicate kits.

Perfboard means a board with a grid of holes where parts and wires are soldered permanently. It requires more custom soldering and inspection than an assembled terminal shield. Avoid buying both whole alternatives now; any small extra filtering board later must have a demonstrated need.

## Selected listing and budget

[Aliex IC Store Mega terminal/prototype shield](https://shopee.ph/product/1391133201/29571601363), screenshot 16 October 2026: **Welded Board**, quantity **one**, **PHP 270**, delivery extra. The separate DIY Kit is not the chosen option. Welded Board is treated as the seller's assembled option; actual supplied soldering/headers remain to inspect.

This replaces the former PHP 350 B02 kit allowance, reducing priced materials by PHP 80. No additional whole perfboard/carrier/header set is needed. The pictured central prototype area is available for later small circuitry if suitable. Do not presume the shield provides additional motor power capability or independent power protection.

The listing advertises full-size Mega 2560/R3 compatibility. Verify connector alignment, underside headers, continuity/pin labels, shorts, USB/reset clearance, board support and power routing before connecting powered electronics. No seller-specific schematic, connector current or manufacturer product number is inferred. No wiring or final assembly has begun.
