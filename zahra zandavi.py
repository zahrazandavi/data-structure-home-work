class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        if self.head is None:
            self.head = Node(coeff, power)
            return

        curr = self.head

        while curr.next is not None:
            if curr.power == power:
                curr.coeff += coeff
                return

            curr = curr.next

        if curr.power == power:
            curr.coeff += coeff
            return

        curr.next = Node(coeff, power)

    def delete(self, power):
        if self.head is None:
            return

        if self.head.power == power:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr and curr.power != power:
            prev = curr
            curr = curr.next

        if curr is not None:
            prev.next = curr.next
            del curr

    def find(self, power):
        curr = self.head
        while curr is not None and curr.power != power:
            curr = curr.next
        return curr

    def size(self):
        curr = self.head
        cntr = 0

        while curr is not None:
            cntr += 1
            curr = curr.next

        return cntr

    def is_empty(self):
        return self.head is None

    def __add__(self, other):
        res = List()
        curr = self.head

        while curr is not None:
            power = curr.power
            coeff = curr.coeff

            other_curr = other.find(curr.power)

            if other_curr is not None:
                coeff += other_curr.coeff

            res.insert(coeff, power)

            curr = curr.next

        curr = other.head

        while curr is not None:
            power = curr.power
            coeff = curr.coeff

            if res.find(power) is None:
                res.insert(coeff, power)

            curr = curr.next

        return res

    def __mul__(self, other):
        res = List()
        curr = self.head

        while curr is not None:
            power = curr.power
            coeff = curr.coeff

            other_curr = other.head

            while other_curr is not None:
                other_power = other_curr.power
                other_coeff = other_curr.coeff

                res.insert(coeff * other_coeff, power + other_power)

                other_curr = other_curr.next

            curr = curr.next

        return res

    def sort(self):
        swapped = True

        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.power < current.next.power:
                    current.power, current.next.power = current.next.power, current.power
                    current.coeff, current.next.coeff = current.next.coeff, current.coeff
                    swapped = True

                current = current.next

    def __str__(self):
        self.sort()

        curr = self.head
        out = ""

        while curr is not None:
            power = curr.power
            coeff = curr.coeff

            if curr == self.head:
                if coeff < 0:
                    out += '-'
            else:
                if coeff < 0:
                    out += '-'
                else:
                    out += '+'

            if abs(coeff) > 1 or power == 0:
                out += str(abs(coeff))

            if power > 0:
                out += 'x'
                if power > 1:
                    out += '^'
                    out += str(power)

            curr = curr.next

        return out


def main():
    p1 = List()

    p1.insert(2, 1)
    p1.insert(3, 0)

    p2 = List()

    p2.insert(4, 2)
    p2.insert(5, 1)
    p2.insert(6, 0)

    print(f"P1: {p1}")
    print(f"P2: {p2}")

    print(f"Addition: {p1 + p2}")
    print(f"Multiplication: {p1 * p2}")


if __name__ == '__main__':
    main()
