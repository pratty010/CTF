/* WARNING: Could not reconcile some variable overlaps */
// On reverse engineering using Ghidra --> disassembled main() code

undefined8 main(void)

{
  undefined8 local_48;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined8 local_18;
  undefined8 local_10;
  
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  local_10 = 0;
  printf("Hmmmm... I think the tablet says: ");
  fgets((char *)&local_48,0x40,stdin);
  if (((((local_28._2_1_ == '4') && (local_38._4_1_ == '3')) && (local_28._4_1_ == 'r')) &&
      ((((local_48._1_1_ == 'T' && (local_38._5_1_ == 'v')) &&
        ((local_48._6_1_ == '0' && ((local_28._7_1_ == '}' && (local_28._6_1_ == 'd')))))) &&
       (local_30._7_1_ == 'r')))) &&
     ((((((local_30._5_1_ == '3' && ((char)local_40 == '3')) && (local_38._6_1_ == 'e')) &&
        ((local_28._3_1_ == '1' && (local_48._5_1_ == 'r')))) &&
       (((char)local_48 == 'H' && (((char)local_28 == '3' && (local_38._2_1_ == '.')))))) &&
      (((((local_40._5_1_ == '4' &&
          (((((local_48._3_1_ == '{' && (local_40._2_1_ == '_')) && ((char)local_38 == '.')) &&
            ((local_48._4_1_ == 'b' && (local_48._7_1_ == 'k')))) && (local_40._7_1_ == 't')))) &&
         (((local_40._6_1_ == 'r' && (local_38._3_1_ == 'n')) &&
          ((local_30._1_1_ == 't' &&
           (((local_38._1_1_ == '.' && (local_40._1_1_ == 'n')) && (local_30._6_1_ == '_')))))))) &&
        (((local_30._2_1_ == '0' && ((char)local_30 == '_')) && (local_40._4_1_ == 'p')))) &&
       ((((local_38._7_1_ == 'r' && (local_30._4_1_ == 'b')) &&
         ((local_28._1_1_ == 'p' &&
          (((local_48._2_1_ == 'B' && (local_30._3_1_ == '_')) && (local_40._3_1_ == '4')))))) &&
        (local_28._5_1_ == '3')))))))) {
    puts("Yes! That\'s right!");
  }
  else {
    puts("No... not that");
  }
  return 0;
}

