# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    l, r = 0, s.length() - 1

    while l < r do
        if !(s[l] =~ /[A-Za-z0-9]/i)
            l += 1
        elsif !(s[r] =~ /[A-Za-z0-9]/i)
            r -= 1
        elsif !(s[l].downcase == s[r].downcase)
            return false
        else
            r -= 1
            l += 1
        end
    end

    return true
end