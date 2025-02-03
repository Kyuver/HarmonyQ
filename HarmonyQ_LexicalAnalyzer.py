import re

input_program = """
connect("MySQL://localhost:3306/mydb");
query MYSQL.db1.users join postgresql.db2.orders on users.id = orders.user_id
sync MYSQL.db1.users to postgresql.db2.users;
if (count > 100) {
    print("High number of users");
} else {
    print("User count is within limits");
}
group sales by region having sum(revenue) > 10000;
update products set price = price * 1.1 where category == "electronics";
delete from logs where severity == "low";
"""

# Define Regular Expression (RE) 
RE_keywords = r'connect|query|join|sync|group|filter|SELECT|order|return|union|intersect|except|fetch|save|update|create_index|delete|insert'
RE_reserved_words = r'True|False|Null|if|else|import|export|function|into|mysql|MYSQL|mongodb|MONGODB|POSTGRESQL|postgresql'
RE_noise_words = r'and|then|do|with|FROM|INTO|by|as|when|WHERE|where|merge|using|between|LIKE|exists|all|any|default|limit|distinct|cascade|validate|track|show'
RE_identifiers = r'[a-zA-Z_][a-zA-Z0-9_]*'
RE_string = r'"[^"]*"|\'[^\']*\'' 
RE_arithmetic_operators = r'\+|\-|\*|\/|\%'
RE_comparison_operators = r'==|!=|<=|>=|<|>'
RE_logical_operators = r'&&|\|\||!'
RE_assignment_operators = r'=|:='
RE_numbers = r'\d+(\.\d+)?'
RE_delimiter = r'[;\(\)\[\]\{\},.:]'
RE_comment = r'#|##'

# Extract strings first before
string_literals = re.findall(RE_string, input_program)

# Replace Strings with Placeholder (for it to not be broken down)
modified_input = input_program
for i, string_literal in enumerate(string_literals):
    modified_input = modified_input.replace(string_literal, f"STRING_LITERAL_{i}")

# A Custom Tokenize for Delimiter specifically
def custom_tokenize(input_text):
    # 
    tokens = []
    current_token = ""
    for char in input_text:
        if re.match(r'\s', char):  # Whitespace
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif re.match(RE_delimiter, char):  # Delimiter
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return tokens

# Tokenize the modified input
input_program_tokens = custom_tokenize(modified_input)

# Replace placeholders with original strings
for i, token in enumerate(input_program_tokens):
    if token.startswith("STRING_LITERAL_"):
        index = int(token.split("_")[-1])
        input_program_tokens[i] = string_literals[index]

print("Tokens:", input_program_tokens)

# Token classification
for token in input_program_tokens:
    if re.fullmatch(RE_string, token):
        print(token, "-------> String")
    elif re.fullmatch(RE_numbers, token):
        print(token, "-------> Numbers")
    elif re.fullmatch(RE_keywords, token):
        print(token, "-------> Keyword")
    elif re.fullmatch(RE_reserved_words, token):
        print(token, "-------> Reserved Word")
    elif re.fullmatch(RE_noise_words, token):
        print(token, "-------> Noise Word")
    elif re.fullmatch(RE_arithmetic_operators, token):
        print(token, "-------> Arithmetic Operator")
    elif re.fullmatch(RE_comparison_operators, token):
        print(token, "-------> Comparison Operator")
    elif re.fullmatch(RE_logical_operators, token):
        print(token, "-------> Logical Operator")
    elif re.fullmatch(RE_assignment_operators, token):
        print(token, "-------> Assignment Operator")
    elif re.fullmatch(RE_comment, token):
        print(token, "-------> Comment")
    elif re.fullmatch(RE_identifiers, token):
        print(token, "-------> Identifier")
    elif re.fullmatch(RE_delimiter, token):
        print(token, "-------> Delimiters")
    else:
        print(token, "-------> Value Unknown")