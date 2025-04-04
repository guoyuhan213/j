from midiutil import MIDIFile


def create_ode_to_joy_with_drums():
    # 创建MIDI文件(3个音轨)
    midi = MIDIFile(3)
    tempo = 112  # 适中的进行曲速度

    # 主旋律音轨(小提琴)
    melody_track = 0
    time = 0
    midi.addTrackName(melody_track, time, "Ode to Joy - Melody")
    midi.addTempo(melody_track, time, tempo)
    midi.addProgramChange(melody_track, 0, time, 40)  # 40=小提琴

    # 钢琴伴奏音轨
    piano_track = 1
    midi.addTrackName(piano_track, time, "Piano Accompaniment")
    midi.addProgramChange(piano_track, 1, time, 0)  # 0=钢琴

    # 鼓组音轨(通道9是打击乐专用通道)
    drum_track = 2
    midi.addTrackName(drum_track, time, "Drum Kit")
    midi.addProgramChange(drum_track, 9, time, 0)  # 通道9, 0=标准鼓组

    # 主旋律音符(完整主题)
    melody = [
        # 第一段
        (64, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),
        (67, 0.5), (65, 0.5), (64, 0.5), (62, 0.5),
        (60, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),
        (64, 1.5), (62, 0.5), (62, 2),

        # 第二段(重复)
        (64, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),
        (67, 0.5), (65, 0.5), (64, 0.5), (62, 0.5),
        (60, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),
        (62, 1.5), (60, 0.5), (60, 2),

        # 第三段(变化)
        (62, 0.5), (62, 0.5), (64, 0.5), (60, 0.5),
        (62, 0.5), (64, 0.5), (65, 0.5), (64, 0.5),
        (60, 0.5), (62, 0.5), (64, 0.5), (65, 0.5),
        (64, 1), (62, 0.5), (60, 0.5), (62, 0.5),
        (55, 2),

        # 第四段(回到主题)
        (64, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),
        (67, 0.5), (65, 0.5), (64, 0.5), (62, 0.5),
        (60, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),
        (62, 1.5), (60, 0.5), (60, 2)
    ]

    # 钢琴伴奏和弦(C大调)
    chords = [
        # 第一段和弦
        ([48, 52, 55], 1), ([50, 53, 57], 1),  # C - Dm
        ([48, 52, 55], 1), ([47, 50, 55], 1),  # C - G7
        ([48, 52, 55], 1), ([50, 53, 57], 1),  # C - Dm
        ([48, 52, 55], 2),  # C (2拍)

        # 第二段和弦(同第一段)
        ([48, 52, 55], 1), ([50, 53, 57], 1),
        ([48, 52, 55], 1), ([47, 50, 55], 1),
        ([48, 52, 55], 1), ([50, 53, 57], 1),
        ([48, 52, 55], 2),

        # 第三段和弦
        ([50, 53, 57], 1), ([48, 52, 55], 1),  # Dm - C
        ([47, 50, 55], 1), ([48, 52, 55], 1),  # G7 - C
        ([50, 53, 57], 1), ([48, 52, 55], 1),  # Dm - C
        ([47, 50, 55], 1), ([43, 48, 52], 1),  # G7 - F (转位)

        # 第四段和弦(同第一段)
        ([48, 52, 55], 1), ([50, 53, 57], 1),
        ([48, 52, 55], 1), ([47, 50, 55], 1),
        ([48, 52, 55], 1), ([50, 53, 57], 1),
        ([48, 52, 55], 2)
    ]

    # 鼓点节奏(标准摇滚节奏)
    # MIDI打击乐音符编号:
    # 36=底鼓, 38=军鼓, 42=闭镲, 46=开镲, 51=骑钹
    drum_pattern = [
        # 每小节8个八分音符(0.5拍)
        (36, 0.5), (42, 0.5), (38, 0.5), (42, 0.5),  # | 咚 嚓 哒 嚓 |
        (36, 0.5), (42, 0.5), (38, 0.5), (42, 0.5),  # | 咚 嚓 哒 嚓 |

        # 可以在副歌部分加入更丰富的节奏
        (36, 0.5), (46, 0.5), (38, 0.5), (42, 0.5),  # | 咚 嚓 哒 嚓 | (开镲)
        (36, 0.5), (42, 0.5), (51, 0.5), (42, 0.5),  # | 咚 嚓 叮 嚓 | (骑钹)
    ]

    # 添加主旋律(小提琴音轨)
    melody_time = 0
    for pitch, duration in melody:
        midi.addNote(melody_track, 0, pitch, melody_time, duration, 100)
        melody_time += duration

    # 添加钢琴伴奏(每小节一个和弦)
    chord_time = 0
    for chord_notes, duration in chords:
        for note in chord_notes:
            midi.addNote(piano_track, 1, note, chord_time, duration, 80)
        chord_time += duration

    # 添加鼓点节奏(循环鼓点模式)
    drum_time = 0
    total_drum_beats = 32  # 总共32小节
    for _ in range(total_drum_beats):
        for i in range(2):  # 每小节重复两次基本鼓点
            for note, duration in drum_pattern:
                midi.addNote(drum_track, 9, note, drum_time, duration, 90)
                drum_time += duration / 2  # 因为鼓点是八分音符

        # 每4小节变化一次鼓点
        if (_ + 1) % 4 == 0:
            # 加入填充节奏
            midi.addNote(drum_track, 9, 38, drum_time, 0.25, 100)  # 军鼓
            midi.addNote(drum_track, 9, 42, drum_time + 0.25, 0.25, 100)  # 闭镲
            midi.addNote(drum_track, 9, 38, drum_time + 0.5, 0.25, 100)  # 军鼓
            midi.addNote(drum_track, 9, 46, drum_time + 0.75, 0.25, 100)  # 开镲
            drum_time += 1

    # 写入文件
    with open("Beethoven-Ode_to_Joy_with_Drums.mid", "wb") as output_file:
        midi.writeFile(output_file)

    print("MIDI文件 'Beethoven-Ode_to_Joy_with_Drums.mid' 已生成!")


if __name__ == "__main__":
    create_ode_to_joy_with_drums()