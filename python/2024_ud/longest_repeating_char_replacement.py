'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'ABABA'
'''

import string as alphabet
from collections import Counter
from typing import List

def characterReplacement(s: str, k: int) -> int:
    '''
    sliding window init first, second 
    '''
    slow = 0
    fast = 1
    count = 0
    deletions_allowed = k
    
    while fast < len(s):
        
        if s[slow] !=  s[fast]:
            if deletions_allowed > 0:
                deletions_allowed -= 1
                fast += 1
            else:
                deletions_allowed = k
                slow += 1
                
        else:
            
            fast += 1
        count = max(fast - slow + 1, count)
    return count


def char_replacement(s: str, k: int) -> int:
    '''
    for a given string s, and a variable k find the longest substring where
    i characters consecutive characters (highest concentration of i chars) + k exceptions exist
    return i

    '''
    slow = 0
    fast = 1
    count = 0
    deletions = k
    s_list = [char for char in s]
    if len(s) > 2 and s[0] != s[1] and s[1] == s[2] and k > 0:
        deletions -= 1
        s_list[0] = s_list[1]
        
    while fast < len(s_list):
        if s_list[slow] != s_list[fast]:
            if deletions > 0:
                deletions -= 1
                fast += 1
            else:
                deletions = k
                slow += 1
                fast = slow +1
        else:
            fast += 1
        count = max(fast - slow , count)
    return count

from string import ascii_uppercase
def replacements_two(s: str, k: int)-> int:
    slow = 0
    fast = 1
    count = 0 
    deletions = k
    char_count = {char: 0 for char in ascii_uppercase}
    char_count[s[slow]] += 1
    char_set = {s[slow]}
    most_common = [s[slow], 1]
    while fast < len(s):
        # debug 
        # ABABAB
        
        
        fst = s[fast]
        # debug
        if s[fast] == most_common[0]:
            char_count[s[fast]] += 1
            most_common[1] = char_count[s[fast]]
            #count = max(len(s[slow:fast+1]) , count)
            #deletions = max(len(s[slow:fast+1]) - most_common[1] - k, 0)
            fast += 1
            
        elif deletions > 0 :
            if s[fast] not in char_set:
                char_set.add(s[fast])
            char_count[s[fast]] += 1
            if char_count[s[fast]] > most_common[1]:
                most_common[0] = s[fast]
                most_common[1] = char_count[s[fast]]
                
            else:
                deletions -= 1
            #count = max(len(s[slow:fast+1]) , count)
            fast += 1
            
        else:
            if slow == len(s) -1:
                break
            char_count[s[slow]] -= 1
            if s[slow] in char_set and char_count[s[slow]] == 0:
                char_set.remove(s[slow])
            
            if s[slow] == most_common[0]:
                most_common[1] -= 1
            #     deletions = max(fast-slow - most_common[1] - k, 0)
            # else:
            #     deletions += 1
            
            slow += 1
        
        count = max(fast-slow+1 , count)
        temp = s[slow:fast+1]
        deletions = max(k - fast-slow+1 + most_common[1] , 0)
        temp_deletions = deletions
        sl = s[slow]
    return count



def char_replace(string_input: str, k: int) -> int:
    most_common = [0, 0]
    slow = 0
    fast = 0
    deletions_available = k
    char_count = {char: 0 for char in alphabet.ascii_uppercase}
    unique_chars = 1
    char_count[string_input[slow]] += 1
    longest = 0
    while fast < len(string_input):
        # advance if dups are available or if unique chars is less than k
        if deletions_available > 0 or unique_chars < k :
            if char_count[string_input[fast]] == 0:
                unique_chars += 1
            char_count[string_input[fast]] += 1
            if char_count[string_input[fast]] > most_common[1]:
                most_common[0] = string_input[fast]
                most_common[1] = char_count[string_input[fast]]
            fast += 1
        else:
            char_count[string_input[slow]] -= 1
            if char_count[string_input[slow]] == 0:
                unique_chars -= 1
            if most_common[0] != string_input[slow]:
                deletions_available -= 1
            slow += 1
        longest = fast - slow
    return longest

from collections import Counter
def replacements_three(s:str, k:int)-> int:
    counter = Counter()
    highest_count = 0
    longest_string = 0
    for index, char in enumerate(s):
        counter[char] += 1
        highest_count = max(highest_count, counter[char])
        if longest_string - highest_count >= k:
            counter[s[index - longest_string]] -= 1
        else:
            longest_string += 1

    return longest_string

def test_repeating_chars() -> bool:
    '''
    something something docstring
    '''
    assert replacements_three('ABAB', 2) == 4

def test_non_repeating():
    '''
    something something docstring
    '''
    assert replacements_three('AABABBA', 1) == 4


def test_only_single_char():
    '''
    something something docstring
    '''
    assert replacements_three('AAAA', 2) == 4

def test_single_char_two():
    '''
    something something docstring
    '''
    assert replacements_three('AAAA', 0) == 4

def test_change_first_char():
    '''
    something something docstring
    '''
    assert replacements_three('ABBB', 2) == 4

def test_long_ass_word():
    '''
    something something docstring
    '''
    assert replacements_three("PNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4) == 7

def test_wtf_long_input():
    '''
    something something docstring
    '''
    assert replacements_three("CCDAEEEDDEBCCDBACFCEDFAECCCCFDEADFECCDEBBEAFEBEEAFDEACBCECEDFBBDECCAAFCDDCABDBAEFABCBAEDCBFAAECEECAEABCBCCABAABECAFEAACEEBCFFFDDCDBCDCACCFFBDBEDBDEDFFECDBDBDABBBDAEACEDFBBAFBABFAEBADCEFDEAFCFDDFFCAFAEEAAEEECBFADCEFADAEEADCBACCDDEFCCCACEBCCEEDBBFFBCEDEFEACBDBBABDCBADDFEADCBEBBCFBCBAECECCCDDADCDBEAFCEADEBBFFACEAAFFDDCEFEEACDFDACFCEAFDCABBBBEBEBDDABEDCAEFCBFEFFABBCFAFCCBDECDBCABFABFABEECEDFFDFFDEBDBBBEEAEFFEDBADAABEEACFCCBEDADFCBDBDDBDCABDFCDECEFBFDFCDCFEBCCDDFABCBBCCCBCABEECBCBCBEADECAFFFCFAEFFFCDADBADFDFFDCBABFADFAAEFBADCCAFEEBFCFEBCFCEDACCADAAEEEBDCADABFBADBAECACBEFAECFFBCFBDEAECEBCFFDCEEEEEAFEBFFAEBBBDBBFFDBFADEECFDEBDBBCEEDBBADDBBDEDDAFEBCEDCAEBEEEDCFEDDACCDDCAEFDECBDCBBEFCFCECAABCFBBACACCEACDCBDBFECBDFFEBBFBABDECAECAFEEDAABEAFBECAACCACEEAADCEFEEBFFCCBDBCCBADDAAAADBFAECFBFACFDECFACDCCBBCADAEBEDDEEDCBDAFDDAAAFECDADBDAACCBDFAEEACFBBDEDDCCEAAEFEBFCAAEDDCFBDEFECBEFACCCDEDAAABEDAECDEEFCDACCBCDFBCADBCFAACCBBDFFBFBCACEABACAFEDCECCBDFAEDCBDCBAAFEDBCCBBFAFAEABFBEEBDCDFECDDDBDDCCBEFCCEDCECFCBEFFFBFBFBFDDCBEDADECCFFAFAEBEAABECFECABDABFBCEDFCCCCADEBCFBECCDFAAFEFEADACDEFFCBACAACFFECAAFDEDECCDFEDADBDAECDFFECAFFFEDEBEDBBBBBABDAEFFFDDDDCCEEEADEBFEAEFDACBFDBFDADEEACECFADACEEDBCECBCEFCBFBDEADAFCDACCFAEFEFAFDFECAABACFFFDCCBBCCDFECEDECDFDBBFACCDFBADFABBFADDFFCAAABEBDFAAEDAACFCCAEECCAFCEEBEEBCCFFEFFDEFBEEFBBFECFADAFFEBAAFBCFBAFBACDFDAEDBEBEEBBFDEDCEFCBBBABCDAEBEFAEBEAFDECABBADBFCEFFFDBAFDBBEBBCAACBFDDCEFEEEDDADBCFCEAACDBFBFDEACDCDFABDACBCAEEDECCDBDBCBACEBBBBADCBFCDDBDFECEECFDFFBDCBAAEBFCFCDFDBBBFCDECBADAFCBFECABACBFDBAFDCDBBBECCDFDFBECEDBCCAEFDAFACEBFDBDFAFCFFACABCAAECCBBEEBDAFAEFFFEBDECBEAECEAECACDBCFEAADBFEADCCEFAFCAADAEEDFBAFACBAFCEACAADDECFBFDBFCCFAABDABFBEEDFDBAFFECBDDCDCBDEBEFDCCBDBFECBFEAFDCDECAFEAAEAABDFDBBFECAECFEBADCFEEDCBDBFDBBECECFBDDBEFAACEABEFCAAFBDACDDFAEEFDAACBEAEAFDAFEECEFECFBABABBCCBFECBBCAFDCEDCBCAEBFBBCCCBBAEFEFBEEDEFCABEFEECCFBAADEFCEFDDDEDDDBBDABEEFECAEEBCCDDFBAEDCBCCEFFBECFBDECAFEEDBECEBACEBFCEFBECEDFABFAADEBACECDEEBDDFAAEFCCFBFCCAEAAEFAEDEEFBADFCDCFAFEDBDADCFFBDBBEDFEDEFDFCAAAFBADDBDCCCCACDDBBFBECCACDAACCBBDFEEBAACAEDEBBDCDEBDADCAADEFFDDAEADDDFBDBAACFDCEEAAAFDEBBFFEBACADCACDEECCCABFDDCAADEAFABCCCEEFEDDDCBEEFFEDFBBAECDEAAADAECEAACBCBBFCFBEEAFFFDEFDDCBDDDAFAFDEBCEEEACACACCBBBCBADDCECBDEDAAADEFDDDEAEBBBEAEFEEBEAABCFCBCAFDCFDDCFDFAABEFCAFEFADBCDDEADEFAFDAFDECBCECEADFCDAECBDBFEAEAACEBFFFAFEEDABBEBCCBAFACEAFFFABCAEAFEDFCBFEAAEDCCBDBFEFFFCDEAEBEBCDCDEEFDBEEAFBBAEEEAABBEDBFACFCACFABAEBAFADBBEBCEBCFECBFDABBAAEDCDECEAADEDBBFAEECCADFCBAFAAFEDAEFDACBDEAABFFAACEFDFCFFCEFACFBDDABCACACDACACDEBACDCDCADEADFBFACEAABCFDCDDAAEFCFEAFCFFAFDCFDEDAEFCEDAFDFFFBECCFEAADEFAACFDEFBEEBCDADDFCDBADBADFFCCCFBBBDDDEEADDADEFDDECFFACCDFCCBBFACFDFBBEFBCEDACACBAECDECBCBCCFEBEEAEECDCDBAADEABFFCFECBBEFACDBFEBAAFBBDFDEEFCCCFEBBBFECCEBDBADBFCDFCDBADCEACCBDCBAAFEEDDFEAEDFEEEEBCAFCDDBCBDDDCABCBFDCBEFCBCEBFDFBCCDBEAABEAFCACDEBEDCAADEDDFFBFEDAFEFACDDCAECEAEBBECBAACADDCBEAFFBCFAFBBAFCDDCEBCAEFEFBABFCBFDDAEFDBFCDFDACFAAAFCECEAEDDBFFBBBEBAAAAADABEDEEBCECCBCBCEEBECDCFDCCDEADFBDACAFFAADCBDAEEABEDBBADAEFCBBAEFEDBBFEAADFAFBABADBBDCDECCDAEBFACDDEECEEBEFFBCEAEDEBDEACCFAEDDDFADCCFDFACFECEFDDCCEECBFDABDFDCBEDDABEFFCDDEDCEBEFAEBFCFBEACCDABDDACBEFBCFCEEEEFEBABBEFCAEEECEBBDBEBDDABEBCCABCFFCDBBAEBBFAABCEBADCCEEADBBEBCCDBAAAFBFBCFFACCFFFDDBFAAEBACACFEBEDACAABAEECFCAABCDABBCEDADFFAABBDDBFDCFEEFADBCCBDAAFCFCBEAECEBFFEDDFCBCCFDEEAABCDFEBFEACDAFCCDCFBCDDAEDFBAAFBCDFFBAAFBCEFAFCBEAEECEDDBBDFFDAFBBFFECAFDAAFDCFDCBBBFCEDCFADFAEEDFEFDCCACACAACCBAEDFDDBEECFDEBFCACBDACBAFFCCEDBBEECBACFCDBEEBAADBCABCFFAFFCBABDBEBCDDEEDEBBDECAEEEBFFFEDFDFECEAFAADDAEAAAACBBDFFACAFFEEFAECDDFDBCBCDEFDFFDDACEEBBFDBBEBAEFDACEEEACAFACCBDFEABEDCADFCFFEEBFFBFAEAFBDEDABEACADEACDDADCCFBCDBFCBDCADBFBBBFECCCEBFDEDEEDBCDCBEEBCEFFEADDFDCABAAEAFCAEACCBDFCEECDCFCABCCDDAFDFACCCFBDCFFFDDBAFCECCCBFCAECABCBFEEDADCFFCFBDAEEDBCABBCFFDBCECBAABEEFFDDAFDEBAAFBDBDEEBACFAEBEECFAEDDFDBBFEDACBADECEBCFCCFCCBEEEBCCFFFEFFAEDBECAFBFBFDDFEBDCECAFFCCBAECCAAFEDDDAFAABADBAFEDAFFEEAFFFBEFBEADEDDFAFEBDFAEBCDDFBCFEEAFDDAAFAAEACBCEACBCBEECFAAEFBBBEFDBBDDCEBBABFEFCABEBDAFDDDFDCCFFFECDFACCAABCDABDABFFBACBAADDCEBBBDFEEFAAADEEEFEDDDFCBCDFDFEFCEEFCBCAEFFCEDAADBDEFEABBEEDBFBECDCACAACCAAAFCEFBBCCEADBFBCFCCCEFABBDADBACACDABBADAFDECFBDABDEBEBFDFCBADAEDFCFFCEDEBBADFDBCFFBFAFDCFEADFFAEDFEBDCCEAABDBDCADABACCAAFEDDFCADAFDFADDCEEAFAAACAFCAAAFEBDBEBACCABCBFCCBCEDADAEAFDAEFDEABCACCCECFDFFCAEBCECAEEDFFEDAEFEBCAAECCFBDDACABCBCEBBADCDDECDBBEFAFCDAFBEDCEDBAEBCADEDFFEECEFDDEFCBBBBEDBBBBCBAEFDDEBDBCCEAAAFADEFACFBABCCFDCBBADCBAEEEEBAEAFCEEFBCFCBFEFDDCBDCDCEAFEAADEEADAEFBBEDBBCECABFCCEBADECACDAECEBECBAAFCBEABCBDFECDECFDBAFDBCBDFEDBEACDBDEBEABFBBEDDBAFBACCDEABDBEDEEFEDDDCDACEBEDBBBFBEFFBCAFBAFFAEAFACCFDFDFCBCDAABDFBBECBFFAABCFCFCAEEBFCCDFFEFEADBCDDDFCEDBFEABDDFBCBEABECBCCACCCCABAAFCABCAFFCCCFCBBEFEEBEECEEBDDEBABAFFEAAADACDFDBEAABFAECADAEBFFBECBEBCEEEBFEAECEEFAFAEFCDECDECFEBFFBAAFADCAAABDBCDABCAAAFBAEDEFFEDABCDBBECBCCDEFBDACFFBFCEAEFBDCADAEEDCBFEDAEEDBBFFFCFEDFDDAADDCAECBBECDDDFBAFEABFDBBBEEDBFAFAADFDCFCBEAFAEBBDDFDFFCBBCFCCBCCEBAFBAFDEAFCAFFCBDDABDFDBAFDEADCBDFCAACAEEFDEABAEDAFBBBFDACBDABFBFBEAEEFEFCCDCECAECECEABBEFABDFAFDABBDFEFFCBDFCFFEEBBFEDFCADDBEADFFDDACCDCDEBADDABBDADAFCACAEDFDFFDCABAABCCEBDEAFBDCBECFFCAAABBECDBFDFBDEDCACDEAADCDFEAEBBBADFECECEAEBEBFDCABEDDBEECEEDFCEDDADAEBCEEDBAFDFACDEDDABDEBDDDAECBFEFCEEDBBBEBADFFCABDFABFBBFCABFFCCADFCBFBABCDFFDCFBACBCCBBDCDCABFDAFBCFAFBDAFAACBFACCCDBEDFADFEEEDCADEFFFDDCECADEFCDEDCCDDFEDFEBCBCABDDFEADFDFFECFFCCBCABEFBDBDAEDACBBFFBDFEEEACDEBDFFCDEFEBFBBEFABBDFDADDBACEEEBAEECEDACCCDDDFBCEEECCDAEDCCCDBCEBDDADAACCFAEEDFBAEECACFFDEBADDDAABBCDACEEBEAFCADEAFFDBAFFEDAFECCAAEBAFACACEDEBCFFFFDEDDEAFEBCEFDCBCBCBCCBADBAACFDFFBFDABDACCBFEEADFECBBCAFCFDADAACFDBAAAEEACCDAFFCFBCAFBDBAECCCFBDFBFCEBEABFEADAADAEAABEDDACBCCDBAFCCFEAAFBBBBFFCBADEBDECFCCADDCCFFBEDCAADDDFDCFBABBEBBFFDDDBCDBCDDAEDFDBCADEDDECBAAAFCDACDEAAEFEACEBCEEAEBEFCEDEDCAAAFBFCDCEFFBCFDCBAFEDACCBFFAFCBADAEFDBDFAABABDCDABDEAAFEBFFCFABBDECEDDBECEEACCDBEEAEBEECDBBBDEEADFDEFDADDBAACBCCDCCFCFEFEBCDABEFBABCDCBFDAACDDFCCFACEBDCFEABACFEBAFECEAABFFDBFFFDACEAECBFDECFDAFCECEBCBFFAEDBEEDFDEBBBCFFEBFFDDCDBDFCCBADCDDBDEACEEDDBECCEFDAFEAABCEDFAEAFCEFDAAECEFDEDDBACDBDFCAECBEFEDADBBBDFFADDCCADBFBAECBACDDBEFDCEDBCFDDFCAEDBCBBDCFBDACFBBEEECFCEBFCFDCAACBBEBEACFCCECCCEFEAEBEBADDACCFCFBCADEEBCBDBFAAFEFBFBBAFAACDDFFBDCECAABEAADAEDCECDEDADFBEACDBBEAACDAABEEDBDADCACFEEABBCBFEDDCDBFDCADCABBECBBCCBDBFEBEBFCCEDBFABDCFFFECFCEEFFBECCCAAFBCBDBDDADCFCEDBEEDAEBCABDFEDFACBFCBEABEFCDBDCFACBBACDFEBCCDBBBCFEADACAEDCCFEAECDAACAFFDFFABFBDCBAEBABDBCFABAAFEFECBAFBCEDCFEAFEDCBCCDDDCEBDFADCEEBABBFAEEACADCABCFAFBBEAFDFBDABBCECAEFEDACCCAEFFACCDADACCFAFEBABACFEFACCAACFFFDCDDDADCEEAABEEBBEFFFBFEECFEBCBFDEBDAAFCBFABFFCBDBDEADACEACBCDCEEFABAFBDDADDADDDAEBDDABBEAFDEDFDACCCFEBCACDDEFBBDACCBCACBDFFCFAABEFFDBFAFDADBDFEFABEFFFCBDEBFDBEECDACFEDCBFDBFEABEEEBADBADDFEAECBCEBAEABBBEEFDCEFBDEADCFBBAFEACBDEDAAEBDABBAAFCBDEFDEABCAFCDECABFDAFBEEDDECBCABBACFEBBACEEEFADEDECFBABECECEBCABAAFBFDADFDEDCBEEAEEAFBFFCCAACCEBCBEEBBABBDAEBDBBEFDEDCABEAAADFCDFDEDFBFDFFDEEEBEACBDDDFDCACAAABBDBFDCDEDFDDFBDDABEFFBCCDFFAFAACCEACEFAEFFCBBEECCBDEADCDBDADEACBFFDFDFDACFDABBEFFDFEDEDEEACDFEEBFCBBDADAEEFFFBFDACBFDBBBDDDDCDFECBDBFAFDEEEDBFDBDEFAFEFDACBEDDAAEBEDCFCABFDAADFEFBACCEBEECECDDBCCDECFEABABEEDDAEBEDCEBABEBBFAEEBCEDEFCDBEEBBCBCEEEEFFFFEDFABFBDECFFFDDBDFCCDBFFDDDEDEBAEFABFCDEDCCDEBBAECCAEEFFFEFCACACDEECBBBBEFBAEFAAFBBCDABEDEEECBDDCFEDAFCFFEAAFEEFBFDCBDDEDBEFECBDFEBFEBDFDEEBCAEBDFDFAEAACEADCCECDECCDFAAFBCEDFEFAEDCFFDAECDAAEBEFEFDCBDCCDCDADBEDECADBBCBEBBABEDEEDEDBBAABCCBBABADEADFCCFDBCACAAFAFCDDFDFFAAAFDFFBDDEFAFFFCAEEEFFACECEDDEDCEFACFEDBDDFABEBFCEBECFFACACAFFBDBCBDBFCEFBDFBEFAEDFCFBCDCCABFEABECFCACBEFFAEAAAEDBFAAEDECBBBEAFDCACDCFDAFCECBCBCCEFFDCACDEEADAADDACCDAFECDFAEEFCDBAEAFFCDBADDFAAFACFEDDADBDFECAECBCFCAEACDDFEABFFEDADCECDFADFCBDFAFCFFEFECABACADCFCCFCDFDFBBCEFDACBBCCDDBADEDDFBACFFAFBBFBECBCCFEBCFABBBDCCCBDBEBDDCBBDFDDBEFCDADAECDEBFDCEDEBBECAABABEDAAECAEEFFDDFBCADCFFCAFCFECFCEBFDECBEEBCCFCCACFAFEBBADAEECCEEECBBDAEEEDCCDCECAEFBAFDABBECFDFBDEFDFAFDEABEFBAAAACCEAFEFABAAEEAAFABFAACBDCCBDFCEBBECECFEBCEBEFACCFEEBDBAEBDAAFBFFBADADECCABFEEABADEFBBFFEFCFFDEEDECAECABBBAFAFDCFCDADACACDDDBFADBDCEADEAAAACDBDADCCEEEBBFADAEEEDABDCEACBBEFEFEADBDEABEEFABDAFBFAEBBDDFCECECDFBEBFBFBCCBABBBAFDBECBADBACDBAACDEBDFFEDEBCACACADBCFEEDDCFBCABACAADCDAAFEADEDDBCCDFFFCAEAFBEBBCEFCEABCCEBBAAFCCDDFDEBEAECEEADDADFDFADDAABDCADEDDAACFCFADDCEDBDCAEFACFBDADECCCFDEFFDCADDEAACFCCEADCAEECCBAABFBDFADDDBBFDDCAEDDBFCCEBFADFBAFCBEECEAFBFADEBCCADCAAEDCCCFACECDADFAEDEBDDAADBBEECEEFEFEEBDBBBACBBBEEFECEFDAAFEDECCAEABCBCAFBFABFBAFDCDEFDDFFCADBDABFEFCCBDEEFBEDDBABACABBAABCBCBCEDAAABFABFDFAACCFDCDFFCFBAFCFDECEBBBBCFEAFABDEDEBECCCDBEABAAAFFEBAFAEDDBEFAFCBAACCABDCCCEFADFCAEFBFABBBECFCCFDCFDDCECFFCBDACCDACDEAEDFCDADCDDCEBCBEBDDAEBBEDDDCBBEBADECCFEAABFDDFECCCCCDEADFBAACCBAEADBDADFABCDDCECDFEDBFFBDFDAEECDBBAABAAFBECFCDDCBFDBFACDBACAFEBFBFFEEDBEABEFEBABDFBBDDEDFABBDBFAFBEAFAEDCABCFCDEFABAFDDABBDAADCEBACEAEADBEBCBBDAFABCEEEADFCABFFCBFCBACEBEACEAABDCCAFFDABFADDCFBDDAFFABAEDADFFBCBABDCDEACCDAAADEAEDEBFDDBADDBACDEABFFCAEBEBDCFDABACECFBBFBEACCDACBDBCEECFFAECEBADEDDFBEEACECBAFDBFFAFBBDCCCEACEEACFABECDBBAAFCDABFADFFACCFDECAFDCEFDDBDFBAFAEBEFEADFCFBDEBCACDBEFDEBAACCADFDDFEDEABBDDAEEADEBDFEBAFDCBCBABCDBAFBCDDEEDDCCEAFFCCADAEDFCAFABEDFECFBBAEEABBDBECCCCCEABFFFBBBFBEDDDEAFFFEAEFFDAADDEABEDDFDBBEFABFECFEECCCCDBAECFCEACEDEBAFCCFDEDCFCCDBDEBCCFBFACCDDAFFBCDEAFEEDCDABBFEAADDECDBFBBFAEDAACABEFFFFECFADEEAEDEEEDFFBCBFABEDABBDBBEDBFEEAAACFFDBBDEEBBBDDDCCEBBCDDFEEFDFBFCBCEFEDCEFFECCBDEEFFECABFACBFCFFEFAECDEABAFECEDEEBAFBBCFFBDAACFBCBFBEFABBBCECCDAACBFBAEABCBBEFEFCDDBBAEFEFBDBAECDBCEAFECEDDECAFAEABCCEAAEACEFFFADDCDEBFDAAACFCCEBEBABCFBDDEECEDBFFFADBDFABDFFCEDCAAEFCDCFECBBCCCDAAABDBAECBABDABEAAFABBFFCDECFCAEFCAFEECBFCAEDCFFDBBFDEBBCBCFBFFFFFECDBEFDEEDFBAFADBBBFFEEFFECFEEEDABBCBDEDEFDCBEBCCAEFFADDAAECCEFEFCFADBAADAFDEBBEECABDEEDCEBCABFBCECDDCCDBBABDABCEDBDCBBDDACECBDEFBEEEEBACBBADFDBACDCDCEBFDEBDAAFCDDBCCCBACAECCAADFBCBACBFBDFFCCCAFBBBBACEFABBEFAAFFDCEEDDDDFBBBADDEEDFBFADCDBDAAAEEFAFFAFCAACFCCFFDAFFCCDCECDEBADACCFFEBCAFAAFBB", 4567) == 5526


#test_long_ass_word()
#test_non_repeating()
#test_repeating_chars()