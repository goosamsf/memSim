inputfiles=(fifo1 fifo2 fifo3 fifo4 fifo5)

for val in "${inputfiles[@]}" 
do
  make ${val}
done

