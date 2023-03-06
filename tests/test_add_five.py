from lib.add_five import *
from lib.greet import *
from lib.check_codeword import *
from lib.report_length import *
from lib.reminder import *
from lib.counter import *
from lib.string_builder import *
from lib.gratitudes import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

def test_greet_returns_name_for_name():
    result = greet('James')
    assert result == "Hello, James!"

def test_check_codeword_all_options():
    result1 = check_codeword('horse')
    assert result1 == 'Correct! Come in.'
    result2 = check_codeword('house')
    assert result2 == "Close, but nope."
    result3 = check_codeword('abracadaniel')
    assert result3 == "WRONG!"

def test_report_length_returns_three_for_ape():
    result = report_length('Ape')
    assert result == "This string was 3 characters long."

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

def test_counter_counts_to_num():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."
    count.add(5)
    result2 = count.report()
    assert result2 == "Counted to 10 so far."

def test_StringBuilder_returns_len_and_str():
    HelloString = StringBuilder()
    HelloString.add("Hello")
    str_len = HelloString.size()
    assert str_len == 5
    result_string = HelloString.output()
    assert result_string == "Hello"

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('thick thighs')
    gratitudes.add('nice eyes')
    result = gratitudes.format()
    assert result == "Be grateful for: thick thighs, nice eyes"