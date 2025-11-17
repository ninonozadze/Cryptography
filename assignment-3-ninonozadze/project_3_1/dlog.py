import math

def discrete_log(p, g, h, max_x):
    current_val = h
    hash_table = {}
    B = int(math.ceil(math.sqrt(max_x)))

    def calculate_mod_inverse(a, m):
        def calculate_extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = calculate_extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        gcd, x, y = calculate_extended_gcd(a % m, m)
        if gcd != 1:
            return None
        return (x % m + m) % m

    mod_inverse_g = calculate_mod_inverse(g, p)

    for x1 in range(B):
        if current_val in hash_table:
            x0 = hash_table[current_val]
            return x0 * B + x1
        hash_table[current_val] = x1
        current_val = (current_val * mod_inverse_g) % p

    current_val = 1
    g_B = pow(g, B, p)

    for x0 in range(B):
        if current_val in hash_table:
            x1 = hash_table[current_val]
            return x0 * B + x1
        current_val = (current_val * g_B) % p

    return None


def main():
    p = int(input().strip())
    g = int(input().strip())
    h = int(input().strip())
    max_x = 1 << 40  # 2^40

    dlog = discrete_log(p, g, h, max_x)
    print(dlog)
    # print(pow(g, dlog, p) == h)

if __name__ == '__main__':
    main()


# time python3 dlog.py
# 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
# 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
# 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
#
# 375374217830
# python3 dlog.py  2.20s user 0.04s system 30% cpu 7.255 total

# --------------------------------------------------------------------------

# ტესტირებისთვის

class DLogTestCase:
    def __init__(self, p, g, h, expected_x):
        self.p = int(p)
        self.g = int(g)
        self.h = int(h)
        self.expected_x = int(expected_x)

    def __repr__(self):
        return (
            f"DLogTestCase(\n"
            f"  p={self.p},\n"
            f"  g={self.g},\n"
            f"  h={self.h},\n"
            f"  expected_x={self.expected_x}\n)"
        )

# შექმნის მაგალითი:
test1 = DLogTestCase(
    "676545834232435476587656984573462534545676587596485374625342435",
    "8765676545684573426343574657485637463565465877646545676534",
    "540499424088884067161517530241440525924380498660849154431804541",
    "6543567654"
)

#  ჩემი ტესტები

# 676545834232435476587656984573462534545676587596485374625342435
# 8765676545684573426343574657485637463565465877646545676534
# 540499424088884067161517530241440525924380498660849154431804541
#
# პასუხი 6543567654

# 2643787280657886490975209524495278347924529719819761432925
# 13407807929942597099574024998205846127479365820592393377723561443721764030073546976
# 2034366567478728126514156339265919208839859622341211969701
# პასუხი 988036620

