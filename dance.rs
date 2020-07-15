// A robot has been given a list of movement instructions. Each instruction
// is either left, right, up or down, followed by a distance to move. The
// robot starts at 0, 0. You want to calculate where the robot will end up
// and return its final position as a list. For example, if the robot is given
// the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
// up 20 left and 40 up from where it started, so you should return [-20, 40].

fn mr_roboto(instructions: &[&str]) -> (i32, i32) {
  return instructions.iter()
    .map(|d_val_str| {
      let [direction, v_str]: [&str] = d_val_str.splitn(2, ' ').collect();
      let val = v_str.parse::<i32>().unwrap();
      return match direction {
        "up" => (0, val),
        "down" => (0, -val),
        "right" => (val, 0),
        "left" => (-val, 0),
        _ => panic!(),
      }
    })
    .fold((0, 0), |(acc_l, acc_r), (cur_l, cur_r)| (acc_l + cur_l, acc_r + cur_r));
}

fn main() {
  let test_1 = mr_roboto(&["right 10", "up 50", "left 30", "down 10"]);
  println!("test1: {:?}", test_1);
}

