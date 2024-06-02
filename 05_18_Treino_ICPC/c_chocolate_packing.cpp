#include <iostream>
using namespace std;

int main() {
    int L, W, H;
    cin >> L >> W >> H;

    int l, w, h;
    cin >> l >> w >> h;

    int p1 = (L / l) * (W / w) * (H / h);
    int p2 = (L / l) * (W / h) * (H / w);
    int p3 = (L / w) * (W / l) * (H / h);
    int p4 = (L / w) * (W / h) * (H / l);
    int p5 = (L / h) * (W / l) * (H / w);
    int p6 = (L / h) * (W / w) * (H / l);

    int max_boxes = max(max(max(p1, p2), max(p3, p4)), max(p5, p6));

    cout << max_boxes << endl;

    return 0;
}
