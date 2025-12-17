# tuples

masala_species=("cinnamon", "cardamom","cloves")
(spice1, spice2, spice3) = masala_species
print(f"main masala species : {spice1}, {spice2}, {spice3} ")
ginger_ratio, cardamom_ratio = 1,2
print(f"Ratio of g: {ginger_ratio} and c: {cardamom_ratio}")
cardamom_ratio, ginger_ratio = ginger_ratio,cardamom_ratio
print(f"Ratio of g: {ginger_ratio} and c: {cardamom_ratio}")


print(f"Is cinnamon in masala species? {"cinnamon" in masala_species}")
