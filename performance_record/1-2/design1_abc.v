// Benchmark "top_809960632_810038711_1598227639_893650103" written by ABC on Thu Jun 13 22:00:03 2024

module top_809960632_810038711_1598227639_893650103 ( 
    n2, n4, n12, n18, n22, n34, n35, n51, n57, n67, n72, n75, n78, n80,
    n6, n9, n42, n48, n56, n65, n68, n77  );
  input  n2, n4, n12, n18, n22, n34, n35, n51, n57, n67, n72, n75, n78,
    n80;
  output n6, n9, n42, n48, n56, n65, n68, n77;
  wire new_n23, new_n24, new_n25, new_n26, new_n27, new_n28, new_n29,
    new_n30, new_n31, new_n32, new_n33, new_n34_1, new_n35_1, new_n37,
    new_n38, new_n39, new_n40, new_n41, new_n42_1, new_n43, new_n44,
    new_n45, new_n46, new_n47, new_n48_1, new_n49, new_n50, new_n51_1,
    new_n52, new_n53, new_n54, new_n55, new_n56_1, new_n57_1, new_n58,
    new_n59, new_n60, new_n61, new_n63, new_n64, new_n65_1, new_n67_1,
    new_n68_1, new_n69, new_n70, new_n71, new_n72_1, new_n73, new_n74,
    new_n75_1, new_n76, new_n77_1, new_n78_1, new_n79, new_n80_1, new_n81,
    new_n83, new_n84, new_n85, new_n86, new_n88, new_n89, new_n91, new_n92,
    new_n93, new_n94;
  NOT  g00(.A(n12), .Y(new_n23));
  AND  g01(.A(n51), .B(new_n23), .Y(new_n24));
  OR   g02(.A(n80), .B(n67), .Y(new_n25));
  NOT  g03(.A(n67), .Y(new_n26));
  OR   g04(.A(n78), .B(new_n26), .Y(new_n27));
  AND  g05(.A(new_n27), .B(n22), .Y(new_n28));
  NAND g06(.A(new_n28), .B(new_n25), .Y(new_n29));
  NOT  g07(.A(n75), .Y(new_n30));
  OR   g08(.A(new_n30), .B(n67), .Y(new_n31));
  AND  g09(.A(n72), .B(n67), .Y(new_n32));
  NOR  g10(.A(new_n32), .B(n22), .Y(new_n33));
  AND  g11(.A(new_n33), .B(new_n31), .Y(new_n34_1));
  XNOR g12(.A(new_n34_1), .B(new_n29), .Y(new_n35_1));
  XOR  g13(.A(new_n35_1), .B(new_n24), .Y(n6));
  OR   g14(.A(n80), .B(n2), .Y(new_n37));
  NOT  g15(.A(n2), .Y(new_n38));
  OR   g16(.A(n78), .B(new_n38), .Y(new_n39));
  AND  g17(.A(new_n39), .B(n18), .Y(new_n40));
  NAND g18(.A(new_n40), .B(new_n37), .Y(new_n41));
  AND  g19(.A(new_n29), .B(n51), .Y(new_n42_1));
  NAND g20(.A(new_n42_1), .B(new_n41), .Y(new_n43));
  OR   g21(.A(new_n30), .B(n2), .Y(new_n44));
  AND  g22(.A(n72), .B(n2), .Y(new_n45));
  NOR  g23(.A(new_n45), .B(n18), .Y(new_n46));
  NAND g24(.A(new_n46), .B(new_n44), .Y(new_n47));
  NAND g25(.A(new_n41), .B(new_n34_1), .Y(new_n48_1));
  AND  g26(.A(new_n48_1), .B(new_n47), .Y(new_n49));
  NAND g27(.A(new_n49), .B(new_n43), .Y(new_n50));
  AND  g28(.A(new_n50), .B(new_n23), .Y(new_n51_1));
  OR   g29(.A(n80), .B(n57), .Y(new_n52));
  NOT  g30(.A(n57), .Y(new_n53));
  OR   g31(.A(n78), .B(new_n53), .Y(new_n54));
  AND  g32(.A(new_n54), .B(n34), .Y(new_n55));
  AND  g33(.A(new_n55), .B(new_n52), .Y(new_n56_1));
  AND  g34(.A(n75), .B(new_n53), .Y(new_n57_1));
  AND  g35(.A(n72), .B(n57), .Y(new_n58));
  OR   g36(.A(new_n58), .B(n34), .Y(new_n59));
  OR   g37(.A(new_n59), .B(new_n57_1), .Y(new_n60));
  XNOR g38(.A(new_n60), .B(new_n56_1), .Y(new_n61));
  XOR  g39(.A(new_n61), .B(new_n51_1), .Y(n9));
  OR   g40(.A(new_n42_1), .B(new_n34_1), .Y(new_n63));
  AND  g41(.A(new_n63), .B(new_n23), .Y(new_n64));
  XOR  g42(.A(new_n47), .B(new_n41), .Y(new_n65_1));
  XOR  g43(.A(new_n65_1), .B(new_n64), .Y(n42));
  NOT  g44(.A(n4), .Y(new_n67_1));
  AND  g45(.A(n75), .B(new_n67_1), .Y(new_n68_1));
  NOT  g46(.A(new_n68_1), .Y(new_n69));
  AND  g47(.A(n72), .B(n4), .Y(new_n70));
  NOR  g48(.A(new_n70), .B(n35), .Y(new_n71));
  AND  g49(.A(new_n71), .B(new_n69), .Y(new_n72_1));
  NOT  g50(.A(new_n72_1), .Y(new_n73));
  NOR  g51(.A(n80), .B(n4), .Y(new_n74));
  NOR  g52(.A(n78), .B(new_n67_1), .Y(new_n75_1));
  NOT  g53(.A(new_n75_1), .Y(new_n76));
  NAND g54(.A(new_n76), .B(n35), .Y(new_n77_1));
  NOR  g55(.A(new_n77_1), .B(new_n74), .Y(new_n78_1));
  OR   g56(.A(new_n56_1), .B(new_n49), .Y(new_n79));
  AND  g57(.A(new_n79), .B(new_n60), .Y(new_n80_1));
  OR   g58(.A(new_n80_1), .B(new_n78_1), .Y(new_n81));
  AND  g59(.A(new_n81), .B(new_n73), .Y(n48));
  OR   g60(.A(new_n56_1), .B(new_n43), .Y(new_n83));
  AND  g61(.A(new_n83), .B(new_n80_1), .Y(new_n84));
  OR   g62(.A(new_n84), .B(n12), .Y(new_n85));
  XOR  g63(.A(new_n78_1), .B(new_n73), .Y(new_n86));
  XOR  g64(.A(new_n86), .B(new_n85), .Y(n65));
  AND  g65(.A(n42), .B(n6), .Y(new_n88));
  AND  g66(.A(new_n88), .B(n9), .Y(new_n89));
  AND  g67(.A(new_n89), .B(n65), .Y(n56));
  AND  g68(.A(new_n41), .B(new_n29), .Y(new_n91));
  NOR  g69(.A(new_n78_1), .B(new_n56_1), .Y(new_n92));
  AND  g70(.A(new_n92), .B(new_n91), .Y(new_n93));
  NAND g71(.A(new_n93), .B(n51), .Y(new_n94));
  NAND g72(.A(new_n94), .B(n48), .Y(n68));
  NOT  g73(.A(new_n93), .Y(n77));
endmodule


