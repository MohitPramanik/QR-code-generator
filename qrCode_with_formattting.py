import qrcode
import matplotlib.pyplot as plt

def normalize_color(color):
    return tuple(c / 255.0 for c in color)

def generate_colored_qr_code(data, qr_color, bg_color, file_path):
    qr_color_normalized = normalize_color(qr_color)
    bg_color_normalized = normalize_color(bg_color)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_matrix = qr.get_matrix()
    qr_size = len(qr_matrix)
    image_size = qr_size * 10

    fig, ax = plt.subplots(figsize=(qr_size, qr_size))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow([[bg_color_normalized] * qr_size] * qr_size)

    for x in range(qr_size):
        for y in range(qr_size):
            if qr_matrix[x][y]:
                ax.add_patch(plt.Rectangle((y - 0.5, qr_size - x - 0.5), 1, 1, color=qr_color_normalized))

    plt.savefig(file_path, bbox_inches='tight', pad_inches=0, dpi=qr_size)
    plt.close()

if __name__ == "__main__":
    data = "Hello"  # Replace this with your desired URL or data
    qr_color = (255, 0, 0)  # Red color for the QR code
    bg_color = (0, 0, 255)  # White background color
    file_path = "featured_code.png"

    generate_colored_qr_code(data, qr_color, bg_color, file_path)
    print(f"Colored QR code generated and saved to {file_path}.")
