// Benchmark "top_809960632_810038711_1598227639_893650103" written by ABC on Tue Jun 11 12:58:18 2024

module top_809960632_810038711_1598227639_893650103 ( 
    n2, n4, n12, n18, n22, n34, n35, n51, n57, n67, n72, n75, n78, n80,
    n6, n9, n42, n48, n56, n65, n68, n77  );
  input  n2, n4, n12, n18, n22, n34, n35, n51, n57, n67, n72, n75, n78,
    n80;
  output n6, n9, n42, n48, n56, n65, n68, n77;
  wire new_n23, new_n24, new_n25, new_n26, new_n27, new_n28, new_n29,
    new_n30, new_n31, new_n32, new_n33, new_n34_1, new_n36, new_n37,
    new_n38, new_n39, new_n40, new_n41, new_n42_1, new_n43, new_n44,
    new_n45, new_n46, new_n47, new_n48_1, new_n49, new_n50, new_n51_1,
    new_n52, new_n53, new_n54, new_n55, new_n56_1, new_n57_1, new_n58,
    new_n59, new_n60, new_n61, new_n62, new_n64, new_n65_1, new_n66,
    new_n68_1, new_n69, new_n70, new_n71, new_n72_1, new_n73, new_n74,
    new_n75_1, new_n76, new_n77_1, new_n78_1, new_n79, new_n80_1, new_n81,
    new_n82, new_n84, new_n85, new_n86, new_n87, new_n88, new_n90, new_n92,
    new_n93, new_n94, new_n95;
  INV  g00(.A(n12), .Y(new_n23));
  AND  g01(.A(n51), .B(new_n23), .Y(new_n24));
  INV  g02(.A(n67), .Y(new_n25));
  OR   g03(.A(n78), .B(new_n25), .Y(new_n26));
  OR   g04(.A(n80), .B(n67), .Y(new_n27));
  AND  g05(.A(new_n27), .B(n22), .Y(new_n28));
  AND  g06(.A(new_n28), .B(new_n26), .Y(new_n29));
  NAND g07(.A(n72), .B(n67), .Y(new_n30));
  AND  g08(.A(n75), .B(new_n25), .Y(new_n31));
  NOR  g09(.A(new_n31), .B(n22), .Y(new_n32));
  AND  g10(.A(new_n32), .B(new_n30), .Y(new_n33));
  XOR  g11(.A(new_n33), .B(new_n29), .Y(new_n34_1));
  XOR  g12(.A(new_n34_1), .B(new_n24), .Y(n6));
  INV  g13(.A(n2), .Y(new_n36));
  OR   g14(.A(n78), .B(new_n36), .Y(new_n37));
  OR   g15(.A(n80), .B(n2), .Y(new_n38));
  AND  g16(.A(new_n38), .B(n18), .Y(new_n39));
  NAND g17(.A(new_n39), .B(new_n37), .Y(new_n40));
  INV  g18(.A(new_n29), .Y(new_n41));
  AND  g19(.A(new_n41), .B(n51), .Y(new_n42_1));
  NAND g20(.A(new_n42_1), .B(new_n40), .Y(new_n43));
  AND  g21(.A(n72), .B(n2), .Y(new_n44));
  INV  g22(.A(new_n44), .Y(new_n45));
  AND  g23(.A(n75), .B(new_n36), .Y(new_n46));
  NOR  g24(.A(new_n46), .B(n18), .Y(new_n47));
  NAND g25(.A(new_n47), .B(new_n45), .Y(new_n48_1));
  NAND g26(.A(new_n40), .B(new_n33), .Y(new_n49));
  AND  g27(.A(new_n49), .B(new_n48_1), .Y(new_n50));
  NAND g28(.A(new_n50), .B(new_n43), .Y(new_n51_1));
  AND  g29(.A(new_n51_1), .B(new_n23), .Y(new_n52));
  INV  g30(.A(n57), .Y(new_n53));
  OR   g31(.A(n78), .B(new_n53), .Y(new_n54));
  OR   g32(.A(n80), .B(n57), .Y(new_n55));
  AND  g33(.A(new_n55), .B(n34), .Y(new_n56_1));
  AND  g34(.A(new_n56_1), .B(new_n54), .Y(new_n57_1));
  AND  g35(.A(n72), .B(n57), .Y(new_n58));
  AND  g36(.A(n75), .B(new_n53), .Y(new_n59));
  OR   g37(.A(new_n59), .B(n34), .Y(new_n60));
  OR   g38(.A(new_n60), .B(new_n58), .Y(new_n61));
  XNOR g39(.A(new_n61), .B(new_n57_1), .Y(new_n62));
  XOR  g40(.A(new_n62), .B(new_n52), .Y(n9));
  OR   g41(.A(new_n42_1), .B(new_n33), .Y(new_n64));
  AND  g42(.A(new_n64), .B(new_n23), .Y(new_n65_1));
  XOR  g43(.A(new_n48_1), .B(new_n40), .Y(new_n66));
  XOR  g44(.A(new_n66), .B(new_n65_1), .Y(n42));
  AND  g45(.A(n72), .B(n4), .Y(new_n68_1));
  INV  g46(.A(new_n68_1), .Y(new_n69));
  INV  g47(.A(n4), .Y(new_n70));
  AND  g48(.A(n75), .B(new_n70), .Y(new_n71));
  NOR  g49(.A(new_n71), .B(n35), .Y(new_n72_1));
  AND  g50(.A(new_n72_1), .B(new_n69), .Y(new_n73));
  NOR  g51(.A(n78), .B(new_n70), .Y(new_n74));
  INV  g52(.A(new_n74), .Y(new_n75_1));
  INV  g53(.A(n35), .Y(new_n76));
  NOR  g54(.A(n80), .B(n4), .Y(new_n77_1));
  NOR  g55(.A(new_n77_1), .B(new_n76), .Y(new_n78_1));
  AND  g56(.A(new_n78_1), .B(new_n75_1), .Y(new_n79));
  OR   g57(.A(new_n57_1), .B(new_n50), .Y(new_n80_1));
  AND  g58(.A(new_n80_1), .B(new_n61), .Y(new_n81));
  NOR  g59(.A(new_n81), .B(new_n79), .Y(new_n82));
  NOR  g60(.A(new_n82), .B(new_n73), .Y(n48));
  AND  g61(.A(n42), .B(n6), .Y(new_n84));
  OR   g62(.A(new_n57_1), .B(new_n43), .Y(new_n85));
  AND  g63(.A(new_n85), .B(new_n81), .Y(new_n86));
  OR   g64(.A(new_n86), .B(n12), .Y(new_n87));
  XNOR g65(.A(new_n79), .B(new_n73), .Y(new_n88));
  XOR  g66(.A(new_n88), .B(new_n87), .Y(n65));
  AND  g67(.A(n65), .B(n9), .Y(new_n90));
  AND  g68(.A(new_n90), .B(new_n84), .Y(n56));
  NOR  g69(.A(new_n79), .B(new_n57_1), .Y(new_n92));
  AND  g70(.A(new_n40), .B(new_n41), .Y(new_n93));
  AND  g71(.A(new_n93), .B(new_n92), .Y(new_n94));
  NAND g72(.A(new_n94), .B(n51), .Y(new_n95));
  NAND g73(.A(new_n95), .B(n48), .Y(n68));
  INV  g74(.A(new_n94), .Y(n77));
endmodule


