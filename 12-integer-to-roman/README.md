<h2><a href="https://leetcode.com/problems/integer-to-roman/">12. Integer to Roman</a></h2><h3>Medium</h3><hr><div><p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:</p>
<ul>
  <li>I can be placed before V (5) and X (10) to make 4 and 9.</li>
	<li>X can be placed before L (50) and C (100) to make 40 and 90. </li>
	<li>C can be placed before D (500) and M (1000) to make 400 and 900.</li>
</ul>

<p>Given an integer, convert it to a roman numeral.</p>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre>
  Input: num = 3
  Output: "III"
  Explanation: 3 is represented as 3 ones.
</pre>
  
<p><strong>Example 2:</strong></p>
<pre>
  Input: num = 58
  Output: "LVIII"
  Explanation: L = 50, V = 5, III = 3.
</pre>
  
<p><strong>Example 3:</strong></p>
<pre>
  Input: num = 1994
  Output: "MCMXCIV"
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<li><code>1 <= num <= 3999</code></li>
</div>
