import pylast

API_KEY = '01af670c1ef137c96453695e39da48cd'
API_SECRET = 'c8c58585be3e6e10925739c41c57b4a4'

lastfm = pylast.LastFMNetwork(API_KEY, API_SECRET)

def getRecent(lastfm, username, limit=200):
    return lastfm.get_user(username).get_recent_tracks(limit=limit)

def artistData(track):
    artist = track.track.get_artist()
    return artist.get_name()

def forwards(recent):
    result = list()
    
    for trackIndex in xrange(0, len(recent) - 2):
        try:
            next = artistData(recent[trackIndex])
            if next == None:
                continue
        except IndexError:
            continue
        
        current = artistData(recent[trackIndex + 1])
        
        if current != next:
            result.append( (current, next) )
    
    return result

def fwdCounts(forwards):
    counts = list()
    
    for forward in forwards:
        counts.append( (forward, forwards.count(forward)) )
        
        for forward2 in forwards:
            try:
                forwards.remove(forward)
            except ValueError:
                break

    counts.sort(key=lambda counts:counts[1], reverse=True)
    return counts

def fader(username, limit):
    try:
        return fwdCounts(forwards(getRecent(lastfm, username, limit)))
    except pylast.WSError:
        return None