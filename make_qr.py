import qrcode
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_single_qr(data_text):
    """단일 QR 코드를 생성하여 PIL 이미지 객체로 반환하는 함수"""
    qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=2,
    )
    qr.add_data(data_text)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white").convert("RGB")

def main():
    # 1. 각각 넣고 싶은 링크나 텍스트와 라벨 설정
    left_label = "GitHub Profile"
    left_url = "https://github.com"

    right_label = "Portfolio / Webtoon"
    right_url = "https://comic.naver.com"

    # 2. 두 개의 QR 코드 이미지 생성
    qr_left = create_single_qr(left_url)
    qr_right = create_single_qr(right_url)

    qr_w, qr_h = qr_left.size

    # 3. 전체 합칠 배경 캔버스 크기 계산 (여백 및 글자 공간 포함)
    margin = 40
    text_height = 50
    canvas_w = (qr_w * 2) + (margin * 3)
    canvas_h = qr_h + text_height + (margin * 2)

    # 흰색 배경 이미지 생성
    canvas = Image.new("RGB", (canvas_w, canvas_h), color="white")
    draw = ImageDraw.Draw(canvas)

    # 4. QR 코드 2개 배치 (왼쪽, 오른쪽)
    left_x = margin
    left_y = margin + text_height
    canvas.paste(qr_left, (left_x, left_y))

    right_x = margin * 2 + qr_w
    right_y = margin + text_height
    canvas.paste(qr_right, (right_x, right_y))

    # 5. 각 QR 코드 위에 텍스트(제목) 작성
    draw.text((left_x + 10, margin), left_label, fill="black")
    draw.text((right_x + 10, margin), right_label, fill="black")

    # 가운데 구분선(세로선) 그리기
    center_x = canvas_w // 2
    draw.line([(center_x, margin), (center_x, canvas_h - margin)], fill="gray", width=2)

    # 6. 결과 파일 저장
    current_dir = Path(__file__).parent
    output_file = current_dir / "dual_qr_card.png"
    canvas.save(str(output_file))

    print("=" * 45)
    print("2분할 QR 코드 카드가 성공적으로 생성되었습니다!")
    print(f"저장 위치: {output_file.name}")
    print("=" * 45)

if __name__ == "__main__":
    main()