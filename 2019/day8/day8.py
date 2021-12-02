def get_data(filename):
    with open(filename, 'r') as f:
        x = f.read().splitlines()
        return x[0]


def create_layers(data, layer_size):
    n = layer_size
    layers = [data[i: i + n] for i in range(0, len(data), n)]
    return layers


def fewest_zeros(layers):
    least_zeros = layers[0]
    for layer in layers:
        if layer.count('0') < least_zeros.count('0'):
            least_zeros = layer
    return least_zeros


def break_apart(input, sep, step):
    return sep.join(input[n:n + step] for n in range(0, len(input), step))


def part_i_and_ii():
    input_data = get_data('input.txt')
    input_layers = create_layers(input_data, 150)
    layer = fewest_zeros(input_layers)
    result = int(layer.count('1')) * int(layer.count('2'))
    print(f'Part I: {result}')
    decoded = decode_image(input_layers)
    decoded_str = ''.join(decoded)
    print(decoded_str)
    final_image = break_apart(decoded_str, '\n', 25)
    print(final_image)


def define_color(layers, el_index):
    for layer in layers:
        if layer[el_index] == '0':
            return '0'
        elif layer[el_index] == '1':
            return '1'


def decode_image(layers):
    # 0 is black
    # 1 is white
    # 2 is transparent
    output = []
    for el_index in range(0, len(layers[0])):
        color = define_color(layers, el_index)
        output.append(color)
    return output
