from midiutil import MIDIFile


def create_ode_to_joy_advanced():
    # 创建MIDI文件（2个音轨）
    midi = MIDIFile(2)
    tempo = 120

    # 主旋律音轨（小提琴）
    melody_track = 0
    time = 0
    midi.addTrackName(melody_track, time, "Melody")
    midi.addTempo(melody_track, time, tempo)
    midi.addProgramChange(melody_track, 0, time, 40)  # 小提琴

    # 伴奏音轨（钢琴）
    accomp_track = 1
    midi.addTrackName(accomp_track, time, "Piano Accompaniment")
    midi.addProgramChange(accomp_track, 1, time, 0)  # 钢琴

    # 主旋律（同简单版）
    melody = [
        (64, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),
        (67, 0.5), (65, 0.5), (64, 0.5), (62, 0.5),
        (60, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),
        (64, 1), (62, 0.5), (62, 1),

        (64, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),
        (67, 0.5), (65, 0.5), (64, 0.5), (62, 0.5),
        (60, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),
        (62, 1), (60, 0.5), (60, 1),

        (62, 0.5), (62, 0.5), (64, 0.5), (60, 0.5),
        (62, 0.5), (64, 0.5), (65, 0.5), (64, 0.5),
        (60, 0.5), (62, 0.5), (64, 0.5), (65, 0.5),
        (64, 1), (62, 0.5), (60, 0.5), (62, 0.5),
        (55, 1),

        (64, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),
        (67, 0.5), (65, 0.5), (64, 0.5), (62, 0.5),
        (60, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),
        (62, 1), (60, 0.5), (60, 1)
    ]

    # 和弦伴奏（每小节一个和弦）
    chords = [
        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 1),  # C
        ([59, 62, 67], 1),  # G7
        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 2),  # C
        ([59, 62, 67], 1),  # G7

        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 1),  # C
        ([59, 62, 67], 1),  # G7
        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 2),  # C

        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 1),  # C
        ([59, 62, 67], 1),  # G7
        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 1),  # C
        ([59, 62, 67], 1),  # G7
        ([55, 60, 64], 1),  # F (转位)

        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 1),  # C
        ([59, 62, 67], 1),  # G7
        ([60, 64, 67], 1),  # C
        ([62, 65, 69], 1),  # Dm
        ([60, 64, 67], 2)  # C
    ]

    # 添加主旋律
    melody_time = 0
    for pitch, duration in melody:
        midi.addNote(melody_track, 0, pitch, melody_time, duration, 100)
        melody_time += duration

    # 添加和弦伴奏（每小节弹奏一次）
    chord_time = 0
    for chord_notes, duration in chords:
        for note in chord_notes:
            midi.addNote(accomp_track, 1, note, chord_time, duration, 70)
        chord_time += duration

    # 写入文件
    with open("欢乐颂(钢琴伴奏).mid", "wb") as output_file:
        midi.writeFile(output_file)

    print("MIDI文件 '欢乐颂(钢琴伴奏).mid' 已生成!")


if __name__ == "__main__":
    create_ode_to_joy_advanced()